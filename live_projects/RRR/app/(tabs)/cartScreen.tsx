import React from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity, Image } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { router } from 'expo-router';
import { useCart } from '../../components/CartContext';

export default function CartScreen() {
  const { cartItems, removeFromCart } = useCart();

  const handleDelete = (id: number) => {
    removeFromCart(id);
  };
;
  const renderItem = ({ item }: { item: any }) => (
    <View style={styles.itemContainer}>
      <Image source={{ uri: item.image }} style={styles.itemImage} />
      <View style={styles.infoContainer}>
        <Text style={styles.itemName}>{item.name}</Text>
        <Text style={styles.itemPrice}>₹ {item.price.toFixed(2)}</Text>
      </View>
      <TouchableOpacity onPress={() => handleDelete(item.id)}>
        <Ionicons name="trash-outline" size={24} color="#fff" />
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={{ flex: 1 }}>
      <Header />
      <View style={styles.container}>
        <FlatList
          data={cartItems}
          renderItem={renderItem}
          keyExtractor={(item) => item.id.toString()}
          contentContainerStyle={styles.listContainer}
          ListEmptyComponent={<Text style={{ color: '#fff' }}>Your cart is empty.</Text>}
        />
        {cartItems.length > 0 && (
          <TouchableOpacity
            style={styles.checkoutButton}
            onPress={() => router.replace('/paymentScreen')}
          >
            <Text style={styles.checkoutText}>Checkout</Text>
          </TouchableOpacity>
        )}
      </View>
      <Footer />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#282828',
    padding: 16,
    marginBottom: 60,
  },
  listContainer: {
    paddingBottom: 100,
  },
    itemContainer: {
        backgroundColor: '#3a3a3a',
        borderRadius: 10,
        padding: 16,
        marginBottom: 12,
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
    },
    itemImage: {
        width: 80,
        height: 80,
        borderRadius: 8,
        resizeMode: 'cover',
        marginRight: 12,
    },
    infoContainer: {
        flex: 1,
        justifyContent: 'center',
    },
    itemName: {
        color: '#fff',
        fontSize: 16,
        marginBottom: 4,
    },
        itemPrice: {
        color: '#ccc',
        fontSize: 14,
    },
  checkoutButton: {
    position: 'absolute',
    bottom: 20,
    left: 16,
    right: 16,
    backgroundColor: '#651613',
    paddingVertical: 14,
    borderRadius: 10,
    alignItems: 'center',
  },
  checkoutText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
