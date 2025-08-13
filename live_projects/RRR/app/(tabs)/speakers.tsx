import React from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';
import Footer from '../../components/Footer';

const speakerData = Array.from({ length: 10 }, (_, i) => ({
  id: i.toString(),
  name: `Speaker ${i + 1}`,
  title: `Title ${i + 1}`,
  image: require('@/assets/images/speaker_placeholder.jpg'),
}));

export default function Speakers() {
  return (
    <SafeAreaProvider>
      <Header />
      <View style={{ flex: 1, marginBottom: 20 }}>
      <View style={styles.container}>
        <Image source={require('@/assets/images/speaker_banner.png')} style={styles.imageTop}
          resizeMode="contain"/>
        <Text style={styles.title}>Speakers</Text>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.cardGrid}>
          {speakerData.map((speaker) => (
            <View key={speaker.id} style={styles.card}>
              <Image source={speaker.image} style={styles.image} />
              <Text style={styles.name}>{speaker.name}</Text>
              <Text style={styles.designation}>{speaker.title}</Text>
            </View>
          ))}
        </View>
      </ScrollView>
        </View>
      <Footer />
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  imageTop: {
    width: 320,
    height: 180,
    borderRadius: 10,
    resizeMode: 'cover',
  },
  container: {
    alignItems: 'center',
    backgroundColor: '#282828',
  },
  title: {
    color: 'white',
    fontSize: 24,
    marginTop: 5,
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
