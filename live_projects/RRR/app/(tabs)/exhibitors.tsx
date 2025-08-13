import React from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';
import Footer from '../../components/Footer';

const exhibitorData = Array.from({ length: 10 }, (_, i) => ({
  id: i.toString(),
  name: `Exhibitor ${i + 1}`,
  title: `Title ${i + 1}`,
  image: require('@/assets/images/speaker_placeholder.jpg'),
}));

export default function Exhibitors() {
  return (
    <SafeAreaProvider>
      <Header />
      <View style={{ flex: 1 }}>
      <View style={styles.container}>
        <Image source={require('@/assets/images/exhibitor_banner.png')}
            style={styles.imageTop} resizeMode="contain"/>
        <Text style={styles.title}>Exhibitors</Text>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.cardGrid}>
          {exhibitorData.map((exhibitor) => (
            <View key={exhibitor.id} style={styles.card}>
              <Image source={exhibitor.image} style={styles.image} />
              <Text style={styles.name}>{exhibitor.name}</Text>
              <Text style={styles.designation}>{exhibitor.title}</Text>
            </View>
          ))}
        </View>
      </ScrollView>
      <Footer />
      </View>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  imageTop: {
    width: '90%',
    height: 180,
    resizeMode: 'cover',
    borderRadius: 0,
  },
  container: {
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#282828',
  },
  title: {
    color: 'white',
    fontSize: 24,
    fontWeight: 'bold',
  },
  scrollContainer: {
    backgroundColor: '#282828',
    paddingBottom: 60,
  },
  cardGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    paddingHorizontal: 10,
  },
  card: {
    width: '45%',
    backgroundColor: '#3a3a3a',
    borderRadius: 10,
    padding: 15,
    marginVertical: 10,
    alignItems: 'center',
  },
  image: {
    width: 100,
    height: 100,
    borderRadius: 50,
    marginBottom: 10,
    resizeMode: 'cover',
  },
  name: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  designation: {
    color: '#ccc',
    fontSize: 14,
    textAlign: 'center',
  },
});
