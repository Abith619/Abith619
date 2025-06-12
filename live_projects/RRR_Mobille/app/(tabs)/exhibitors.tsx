import React from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';

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
      <View style={styles.container}>
        <Image source={require('@/assets/images/speakers_title.jpg')} style={styles.imageTop} resizeMode="cover"/>
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
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  imageTop: {
    width: 370,
    height: 180,
    borderRadius: 10,
    marginBottom: 10,
    resizeMode: 'cover',
  },
  container: {
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#282828',
  },
  title: {
    color: 'white',
    fontSize: 24,
    marginTop: 20,
    marginBottom: 10,
  },
  scrollContainer: {
    backgroundColor: '#282828',
    paddingBottom: 20,
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
