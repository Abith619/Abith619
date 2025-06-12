import React, { useRef, useState } from 'react';
import { View, Image, TouchableOpacity, StyleSheet, Text, Pressable, Animated } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';

const menuWidth = 250;

export default function Header() {
  const [menuVisible, setMenuVisible] = useState(false);
  const slideAnim = useRef(new Animated.Value(menuWidth)).current;
  const router = useRouter();

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

  type KnownRoutes = '/' | '/membership' | '/agenda' | '/speakers' | '/sponsors' | '/attendees' | '/exhibitors' | '/shop';

  const handleMenuSelect = (route: KnownRoutes) => {
    toggleMenu();
    router.push(route);
  };

  return (
    <>
      <View style={styles.header}>
        <Image source={require('@/assets/images/logo.png')} style={styles.logo} />
        <TouchableOpacity onPress={toggleMenu}>
          <Ionicons name="menu" size={28} color="#fff" />
        </TouchableOpacity>
      </View>

      {menuVisible && (
        <Pressable style={styles.overlay} onPress={toggleMenu}>
          <Animated.View
              style={[styles.sideMenu, { right: slideAnim, width: menuWidth }]}>
            <Text style={styles.menuItem} onPress={() => handleMenuSelect('/' as const)}>Home</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/membership' as const)}>Membership</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/agenda' as const)}>Agenda</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/speakers' as const)}>Speakers</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/attendees' as const)}>Attendees</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/exhibitors' as const)}>Exhibitors</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/sponsors' as const)}>Sponsors</Text>
              <Text style={styles.menuItem} onPress={() => handleMenuSelect('/shop' as const)}>Shop</Text>
            {/* <Text style={[styles.menuItem, { color: '#aaa' }]} onPress={toggleMenu}>Close</Text> */}
          </Animated.View>
        </Pressable>
      )}
    </>
  );
}

const styles = StyleSheet.create({
  header: {
    backgroundColor: '#282828',
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 16,
    zIndex: 2,
  },
  logo: {
    width: 115,
    height: 80,
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
