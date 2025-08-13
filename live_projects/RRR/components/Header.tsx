import React, { useRef, useState } from 'react';
import { View, Image, TouchableOpacity, StyleSheet, Text, Pressable, Animated } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import { useUser } from '../components/UserContext';
import AsyncStorage from '@react-native-async-storage/async-storage';

const menuWidth = 250;

export default function Header() {
  const [menuVisible, setMenuVisible] = useState(false);
  const slideAnim = useRef(new Animated.Value(menuWidth)).current;
  const router = useRouter();
  const { user, setUser } = useUser();

  const handleLogout = async () => {
  try {
    await AsyncStorage.removeItem('session_id');
    await AsyncStorage.removeItem('user_info');
    setUser(null);
    router.replace('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  const toggleMenu = () => {
    if (menuVisible) {
      Animated.timing(slideAnim, {
        toValue: menuWidth,
        duration: 300,
        useNativeDriver: false,
      }).start(() => setMenuVisible(false));
    } else {
      setMenuVisible(true);
      Animated.timing(slideAnim, {
        toValue: 0,
        duration: 300,
        useNativeDriver: false,
      }).start();
    }
  };

  type KnownRoutes = '/' | '/membership' | '/agenda' | '/speakers' | '/sponsors' | '/attendees' | '/exhibitors' | '/shop' | '/login' | '/ShopScreen' | '/cartScreen';

  const handleMenuSelect = (route: KnownRoutes) => {
    toggleMenu();
    router.push(route);
  };

  return (
    <>
      <View style={styles.header}>
        <Image source={require('@/assets/images/logo.png')} style={styles.logo} />

        <View style={styles.iconGroup}>
          <TouchableOpacity onPress={() => console.log('Notifications')}>
            <Ionicons name="notifications-outline" size={24} color="#fff" style={styles.icon} />
          </TouchableOpacity>

          <TouchableOpacity onPress={toggleMenu}>
            <Ionicons name="menu" size={28} color="#fff" />
          </TouchableOpacity>
        </View>
      </View>

      {menuVisible && (
        <Pressable style={styles.overlay} onPress={toggleMenu}>
          <Animated.View style={[styles.sideMenu, { transform: [{ translateX: slideAnim }], width: menuWidth }]}>
            <View style={{ position: 'relative' }}>
              <TouchableOpacity
                style={styles.editLink}
                onPress={() => router.push('/MyAccountScreen')}
              >
                <Text style={styles.editText}>Edit</Text>
              </TouchableOpacity>

              <View style={styles.profileContainer}>
                <Image
                  source={
                    user?.image
                      ? { uri: user.image }
                      : require('@/assets/images/profile.jpg')
                  }
                  style={styles.profileImage}
                />
                <View style={styles.profileTextContainer}>
                  <Text style={styles.profileName}>{user?.name || 'Guest User'}</Text>
                  <Text style={styles.profileEmail}>{user?.login || 'guest@example.com'}</Text>
                </View>
              </View>
            </View>

            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/')}>Home</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/membership')}>Membership</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/agenda')}>Agenda</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/speakers')}>Speakers</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/attendees')}>Attendees</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/exhibitors')}>Exhibitors</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/sponsors')}>Sponsors</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/shop')}>Shop</Text>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/ShopScreen')}>E-Shop</Text>
            <TouchableOpacity onPress={handleLogout} style={styles.logoutButton}>
              <Text style={styles.logoutButtonText}>Logout</Text>
            </TouchableOpacity>
          </Animated.View>
        </Pressable>
      )}
    </>
  );
}

const styles = StyleSheet.create({
  logoutButton: {
    backgroundColor: '#e74c3c',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 8,
    marginTop: 20,
    alignSelf: 'center',
  },
  logoutButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  editLink: {
    position: 'absolute',
    top: 4,
    right: 10,
    zIndex: 1,
  },
  editText: {
    color: '#F02121',
    fontSize: 13,
    fontWeight: '600',
  },
  profileContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    borderBottomColor: '#444',
    borderBottomWidth: 1,
    marginBottom: 10,
  },
  profileImage: {
    width: 50,
    height: 50,
    borderRadius: 25,
    marginRight: 12,
  },
  profileTextContainer: {
    flex: 1,
  },
  profileName: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  profileEmail: {
    color: '#ccc',
    fontSize: 10,
  },
  icon: {
    marginRight: 16,
  },
  iconGroup: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 16,
  },
  header: {
    backgroundColor: '#282828',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingTop: 40,
  },
  logo: {
    height: 60,
    width: 100,
    resizeMode: 'contain',
  },
  overlay: {
    position: 'absolute',
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    backgroundColor: 'rgba(0,0,0,0.5)',
    zIndex: 999,
  },
  sideMenu: {
    position: 'absolute',
    left: 110,
    top: 0,
    bottom: 0,
    backgroundColor: '#222',
    paddingVertical: 60,
    paddingHorizontal: 20,
    zIndex: 1000,
  },
  menuItem: {
    color: '#fff',
    fontSize: 18,
    marginBottom: 20,
  },
});
