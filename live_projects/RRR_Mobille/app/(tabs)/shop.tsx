import React, { useEffect, useState } from 'react';
import { View, Text, Image, TouchableOpacity, FlatList, StyleSheet, ActivityIndicator } from 'react-native';
import { Picker } from '@react-native-picker/picker';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';
import axios from 'axios';

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

  useEffect(() => {
    axios.get('https://rrr-mobile.binarywavesolutions.com/api/vendors').then(res => setVendors(res.data));
  }, []);

  useEffect(() => {
    setLoading(true);
    const url = selectedVendor
      ? `https://rrr-mobile.binarywavesolutions.com/api/products?vendor=${selectedVendor}`
      : 'https://rrr-mobile.binarywavesolutions.com/api/products';
    axios.get(url).then(res => {
      setProducts(res.data);
      setLoading(false);
    });
  }, [selectedVendor]);

  const renderItem = ({ item }: { item: Product }) => (
    <View style={styles.card}>
      <Image source={{ uri: item.image }} style={styles.image} />
      <Text style={styles.title}>{item.name}</Text>
      <Text style={styles.price}>₹ {item.price}</Text>
      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Add to Cart</Text>
      </TouchableOpacity>
    </View>
  );

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
                <ActivityIndicator size="large" color="#0000ff" />
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
    </SafeAreaProvider>
  );
};

export default ShopPage;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
    backgroundColor: '#fff',
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
