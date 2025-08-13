import React from 'react';
import { View, TouchableOpacity, StyleSheet, Text } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { router } from 'expo-router';
import { useCart } from './CartContext';

export default function CustomFooter() {
  const { cartItems } = useCart();
  return (
    <View style={styles.footer}>
      <TouchableOpacity onPress={() => router.replace('/')}>
        <Ionicons name="home-outline" size={28} color="#651613" />
      </TouchableOpacity>

      <TouchableOpacity onPress={() => router.replace('/shop')}>
        <Ionicons name="search-outline" size={28} color="#651613" />
      </TouchableOpacity>

      <TouchableOpacity onPress={() => router.replace('/cartScreen')} style={styles.iconContainer}>
        <Ionicons name="cart-outline" size={28} color="#651613" />
        {cartItems.length > 0 && (
          <View style={styles.badge}>
            <Text style={styles.badgeText}>{cartItems.length}</Text>
          </View>
        )}
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  footer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    backgroundColor: '#fff',
    paddingVertical: 12,
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: -2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  iconContainer: {
    position: 'relative',
    padding: 5,
  },
  badge: {
    position: 'absolute',
    right: -6,
    top: -4,
    backgroundColor: '#F02121',
    borderRadius: 10,
    minWidth: 18,
    height: 18,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 4,
  },
  badgeText: {
    color: '#fff',
    fontSize: 10,
    fontWeight: 'bold',
  },
});
