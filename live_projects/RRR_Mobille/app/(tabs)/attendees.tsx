import React from 'react';
import { View, Text, StyleSheet, Image, ScrollView } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';

const attendeeData = Array.from({ length: 20 }, (_, i) => ({
  id: i.toString(),
  name: `Attendee ${i + 1}`,
  image: require('@/assets/images/speaker_placeholder.jpg'),
}));

export default function Attendees() {
  return (
    <SafeAreaProvider>
      <Header />
      <View style={styles.container}>
        <Image
            source={require('@/assets/images/membership.png')}
            resizeMode="cover"
            style={styles.imageCover}
            />
        <Text style={styles.title}>Attendees</Text>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.grid}>
          {attendeeData.map((attendee) => (
            <View key={attendee.id} style={styles.card}>
              <Image source={attendee.image} style={styles.image} />
              <Text style={styles.name}>{attendee.name}</Text>
            </View>
          ))}
        </View>
      </ScrollView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
    imageCover: {
        width: '100%',
        height: 200,
        borderRadius: 10,
        marginBottom: 20,
    },
  container: {
    backgroundColor: '#282828',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    color: 'white',
    fontSize: 24,
    fontWeight: 'bold',
  },
  scrollContainer: {
    backgroundColor: '#282828',
    paddingBottom: 20,
    paddingHorizontal: 10,
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  card: {
    width: '47%',
    backgroundColor: '#3a3a3a',
    borderRadius: 10,
    padding: 15,
    marginVertical: 10,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 3,
    elevation: 4,
  },
  image: {
    width: 70,
    height: 70,
    borderRadius: 35,
    marginBottom: 10,
    resizeMode: 'cover',
  },
  name: {
    color: '#fff',
    fontSize: 16,
    textAlign: 'center',
  },
});
