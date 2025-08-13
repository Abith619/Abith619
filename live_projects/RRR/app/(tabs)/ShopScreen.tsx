import Header from '../../components/Header';
import Footer from '../../components/Footer';
import React from 'react';
import { View, Text, ScrollView, FlatList, Image, StyleSheet, Dimensions, TouchableOpacity, } from 'react-native';

const { width } = Dimensions.get('window');

type Product = {
  id: string;
  title: string;
  image: any;
};

type Category = {
  id: string;
  title: string;
  icon: any;
};

const newArrivals: Product[] = [
  { id: '1', title: 'Sneakers', image: require('@/assets/images/sneakers.png') },
  { id: '2', title: 'Shirt', image: require('@/assets/images/shirt.jpg') },
  { id: '3', title: 'T-Shirt', image: require('@/assets/images/tshirt.jpg') },
];

const bestSellers: Product[] = [
  { id: '1', title: 'Smart Watch', image: require('@/assets/images/cap.jpg') },
  { id: '2', title: 'Jacket', image: require('@/assets/images/sneakers.png') },
  { id: '3', title: 'Shoes', image: require('@/assets/images/shirt.jpg') },
];

const categories: Category[] = [
  { id: '1', title: 'Clothing', icon: require('@/assets/images/sneakers.png') },
  { id: '2', title: 'Shoes', icon: require('@/assets/images/shirt.jpg') },
  { id: '3', title: 'Accessories', icon: require('@/assets/images/tshirt.jpg') },
  { id: '4', title: 'Watches', icon: require('@/assets/images/cap.jpg') },
  { id: '5', title: 'Gadgets', icon: require('@/assets/images/sneakers.png') },
  { id: '6', title: 'Home', icon: require('@/assets/images/shirt.jpg') },
  { id: '7', title: 'Beauty', icon: require('@/assets/images/tshirt.jpg') },
  { id: '8', title: 'Fitness', icon: require('@/assets/images/cap.jpg') },
  { id: '9', title: 'Kids', icon: require('@/assets/images/sneakers.png') },
];

const ShopScreen: React.FC = () => {
  const renderProductCard = ({ item }: { item: Product }) => (
    <View style={styles.card}>
      <Image source={item.image} style={styles.cardImage} />
      <Text style={styles.cardText}>{item.title}</Text>
    </View>
  );

  const renderCategory = ({ item }: { item: Category }) => (
    <TouchableOpacity style={styles.categoryCard}>
      <Image source={item.icon} style={styles.categoryIcon} />
      <Text style={styles.categoryText}>{item.title}</Text>
    </TouchableOpacity>
  );

  return (
    <View style={{ flex: 1 }}>
        <Header />
        <ScrollView contentContainerStyle={styles.container}>
            <Text style={styles.sectionTitle}>New Arrivals</Text>
            <FlatList
                horizontal
                showsHorizontalScrollIndicator={false}
                data={newArrivals}
                renderItem={renderProductCard}
                keyExtractor={(item) => item.id}
                contentContainerStyle={styles.horizontalList}
            />

            <Image
                source={require('@/assets/images/banner1.jpg')}
                style={styles.bannerImage}
                resizeMode="cover"
            />

            {/* Category Grid */}
            <Text style={styles.sectionTitle}>Shop by Category</Text>
            <FlatList
                data={categories}
                renderItem={renderCategory}
                keyExtractor={(item) => item.id}
                numColumns={3}
                columnWrapperStyle={{ justifyContent: 'space-between' }}
                scrollEnabled={false}
            />

            {/* Best Sellers */}
            <Text style={styles.sectionTitle}>Best Sellers</Text>
            <FlatList
                horizontal
                showsHorizontalScrollIndicator={false}
                data={bestSellers}
                renderItem={renderProductCard}
                keyExtractor={(item) => item.id}
                contentContainerStyle={styles.horizontalList}
            />

            {/* Final Banner */}
            <Image
                source={require('@/assets/images/banner.jpg')}
                style={styles.bannerImage}
                resizeMode="cover"
            />
        </ScrollView>
        <Footer />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 16,
    backgroundColor: '#fff',
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginVertical: 12,
  },
  horizontalList: {
    paddingBottom: 10,
  },
  card: {
    width: 140,
    marginRight: 16,
    backgroundColor: '#f8f8f8',
    borderRadius: 10,
    alignItems: 'center',
    padding: 10,
  },
  cardImage: {
    width: 100,
    height: 100,
    resizeMode: 'contain',
  },
  cardText: {
    marginTop: 8,
    fontSize: 14,
    textAlign: 'center',
  },
  bannerImage: {
    width: width - 32,
    height: 160,
    borderRadius: 10,
    marginVertical: 16,
  },
  categoryCard: {
    width: '30%',
    marginBottom: 16,
    alignItems: 'center',
  },
  categoryIcon: {
    width: 60,
    height: 60,
    marginBottom: 8,
    resizeMode: 'contain',
  },
  categoryText: {
    fontSize: 13,
    textAlign: 'center',
  },
});

export default ShopScreen;
