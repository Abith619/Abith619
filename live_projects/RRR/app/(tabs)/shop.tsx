import AsyncStorage from '@react-native-async-storage/async-storage';
import { Picker } from '@react-native-picker/picker';
import React, { useEffect, useState } from 'react';
import { ActivityIndicator, FlatList, Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Footer from '../../components/Footer';
import Header from '../../components/Header';
import api from '../../components/api';
import { useRouter } from 'expo-router';
import { useCart } from '../../components/CartContext';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
}

interface Vendor {
  id: number;
  name: string;
}

const ShopPage: React.FC = () => {
  const [vendors, setVendors] = useState<Vendor[]>([]);
  const [selectedVendor, setSelectedVendor] = useState<string>('');
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [addedToCart, setAddedToCart] = useState<Set<number>>(new Set());
  const router = useRouter();
  const { addToCart } = useCart();

  useEffect(() => {
    api.get('/api/vendors').then(res => setVendors(res.data));
  }, []);

  useEffect(() => {
    setLoading(true);
    const url = selectedVendor
      ? `/api/products?vendor=${selectedVendor}`
      : '/api/products';
    api.get(url).then(res => {
      setProducts(res.data);
      setLoading(false);
    });
  }, [selectedVendor]);

  const handleAddToCart = async (item: Product, quantity: number = 1) => {
    try {
      const userInfoRaw = await AsyncStorage.getItem('user_info');
      if (!userInfoRaw) {
        console.warn('User not logged in');
        return;
      }

      const userInfo = JSON.parse(userInfoRaw);
      const userId = userInfo.id;

      const response = await api.post(
        '/api/cart/add',
        {
          user_id: userId,
          product_id: item.id,
          quantity: quantity,
        },
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );

      console.log('📦 Cart Response:', response.data);

      if (response.data?.status === 'success') {
        console.log('✅ Product added to cart:', response.data);
        setAddedToCart(prev => new Set(prev).add(item.id));
        addToCart({
          id: item.id,
          name: item.name,
          price: item.price,
          image: item.image,
        });
      } else {
        console.warn('⚠️ Failed to add product to cart:', response.data?.message || 'Unknown error');
      }
    } catch (error: any) {
      console.error('❌ Error adding to cart:', error?.response?.data || error.message || error);
    }
  };


  const renderItem = ({ item }: { item: Product }) => {
  const isAdded = addedToCart.has(item.id);

  return (
    <View style={styles.card}>
      <Image source={{ uri: item.image }} style={styles.image} />
      <Text style={styles.title}>{item.name}</Text>
      <Text style={styles.price}>₹ {item.price}</Text>

      {isAdded ? (
        <TouchableOpacity
          style={[styles.button]}
          onPress={() => router.push('/cartScreen')}
        >
          <Text style={styles.buttonText}>View Cart</Text>
        </TouchableOpacity>
      ) : (
        <TouchableOpacity style={styles.button} onPress={() => handleAddToCart(item)}>
          <Text style={styles.buttonText}>Add to Cart</Text>
        </TouchableOpacity>
      )}
    </View>
  );
};


  return (
    <SafeAreaProvider>
        <Header />
            <View style={styles.container}>
            <Picker
                selectedValue={selectedVendor}
                onValueChange={(itemValue) => setSelectedVendor(itemValue)}
                style={styles.picker}
              >
                <Picker.Item label="All Vendors" value="" />
                  {vendors.map((vendor) => (
                <Picker.Item key={vendor.id} label={vendor.name} value={vendor.id.toString()} />
                ))}
            </Picker>

            {loading ? (
                <ActivityIndicator size="large" color="#F02121" />
            ) : (
                <FlatList
                data={products}
                renderItem={renderItem}
                keyExtractor={(item) => item.id.toString()}
                numColumns={2}
                columnWrapperStyle={styles.row}
                contentContainerStyle={styles.list}
                />
            )}
        </View>
        <Footer />
    </SafeAreaProvider>
  );
};

export default ShopPage;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#282828',
  },
  picker: {
    marginBottom: 10,
    backgroundColor: '#f2f2f2',
  },
  list: {
    paddingBottom: 100,
  },
  row: {
    justifyContent: 'space-between',
  },
  card: {
    backgroundColor: '#f9f9f9',
    borderRadius: 10,
    padding: 10,
    marginBottom: 10,
    width: '48%',
    alignItems: 'center',
    elevation: 2,
  },
  image: {
    width: '100%',
    height: 120,
    borderRadius: 10,
    resizeMode: 'cover',
    marginBottom: 5,
  },
  title: {
    fontWeight: 'bold',
    fontSize: 14,
    textAlign: 'center',
  },
  price: {
    color: 'red',
    fontSize: 14,
    marginVertical: 5,
  },
  button: {
    backgroundColor: '#F02121',
    borderRadius: 5,
    paddingVertical: 5,
    paddingHorizontal: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 12,
  },
});
