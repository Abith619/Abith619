import React from 'react';
import { View, Image, StyleSheet, Text } from 'react-native';

const App = () => {
  return (
    <View style={styles.container}>
      <Image source={require('./src/img/home.png')} style={styles.image} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'start',
    alignItems: 'center',
    backgroundColor: '#282828',
  },
  image: {
    width: 300,
    height: 400,
    resizeMode: 'contain',
  },
});

export default App;