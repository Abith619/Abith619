import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

const MyAccountScreen = () => {
  return (
    <View style={{ flex: 1 }}>
      <Header />
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.profileContainer}>
            <Image
                source={require('@/assets/images/profile.jpg')}
                style={styles.profileImage}
            />
            <View style={styles.profileTextContainer}>
                <Text style={styles.profileName}>John Doe</Text>
                <Text style={styles.profileEmail}>johndoe@example.com</Text>
            </View>
            <TouchableOpacity style={styles.editIcon} >
                <Ionicons name="create-outline" size={20} color="#fff" />
            </TouchableOpacity>
        </View>

        <View style={styles.menuContainer}>
            <TouchableOpacity style={styles.menuItem} >
                <Ionicons name="person-outline" size={22} color="#fff" />
                <Text style={styles.menuText}>Your Details</Text>
            </TouchableOpacity>

            <TouchableOpacity style={styles.menuItem} >
                <Ionicons name="receipt-outline" size={22} color="#fff" />
                <Text style={styles.menuText}>Orders</Text>
            </TouchableOpacity>

            <TouchableOpacity style={styles.menuItem} >
                <Ionicons name="document-text-outline" size={22} color="#fff" />
                <Text style={styles.menuText}>Invoices</Text>
            </TouchableOpacity>
        </View>
        </ScrollView>
        <Footer />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#1e1e1e',
    flexGrow: 1,
  },
  profileContainer: {
    backgroundColor: '#2e2e2e',
    padding: 16,
    borderRadius: 10,
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 30,
    position: 'relative',
  },
  profileImage: {
    width: 60,
    height: 60,
    borderRadius: 30,
  },
  profileTextContainer: {
    marginLeft: 16,
    flex: 1,
  },
  profileName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
  },
  profileEmail: {
    fontSize: 14,
    color: '#ccc',
  },
  editIcon: {
    position: 'absolute',
    top: 10,
    right: 10,
  },
  menuContainer: {
    backgroundColor: '#2e2e2e',
    borderRadius: 10,
    paddingVertical: 10,
  },
  menuItem: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 14,
    borderBottomWidth: 1,
    borderBottomColor: '#444',
  },
  menuText: {
    marginLeft: 16,
    fontSize: 16,
    color: '#fff',
  },
});

export default MyAccountScreen;
