import React, { useEffect, useRef } from "react";
import { View, Text, StyleSheet, Image, ScrollView, Animated } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';
import Footer from '../../components/Footer';

type AnimatedCardProps = {
  children: React.ReactNode;
  delay?: number;
  style?: object;
};

const AnimatedCard = ({ children, delay = 0, style = {} }: AnimatedCardProps) => {
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const translateY = useRef(new Animated.Value(20)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 400,
      delay,
      useNativeDriver: true,
    }).start();

    Animated.timing(translateY, {
      toValue: 0,
      duration: 400,
      delay,
      useNativeDriver: true,
    }).start();
  }, [delay, fadeAnim, translateY]);

  return (
    <Animated.View
      style={[
        styles.card,
        style,
        {
          opacity: fadeAnim,
          transform: [{ translateY }],
        },
      ]}
    >
      {children}
    </Animated.View>
  );
};

export default function Sponsors() {
    return(
        <SafeAreaProvider>
            <Header />
            <View style={{ flex: 1, marginBottom: 50 }}>
            <View style={styles.container}>
                <Image source={require('@/assets/images/sponsors_banner.png')}
                    style={styles.imageTop} resizeMode="contain"/>
                    <Text style={styles.title}>Sponsors</Text>
            </View>
              <ScrollView>
                  <View style={styles.cardGrid}>
                  <AnimatedCard delay={100}>
                      <Image
                      source={require('@/assets/images/kash_logo.png')}
                      style={styles.sponsorLogo}
                      resizeMode="contain"
                      />
                  </AnimatedCard>

                  {Array.from({ length: 11 }).map((_, index) => (
                      <AnimatedCard key={index} delay={200 + index * 100}>
                      <Text style={styles.becomeSponsorText}>Become a Sponsor</Text>
                      </AnimatedCard>
                  ))}
                  </View>
              </ScrollView>
            </View>
            <Footer />
        </SafeAreaProvider>
    );
}

const styles = StyleSheet.create({
  cardGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    backgroundColor: '#282828',
    paddingHorizontal: 10,
    marginBottom: 15,
  },
  card: {
    width: '45%',
    height: 110,
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginVertical: 10,
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 4,
  },
  sponsorLogo: {
    width: 80,
    height: 80,
    resizeMode: 'contain',
    marginBottom: 10,
  },
  becomeSponsorText: {
    color: '#0a0a0a',
    fontSize: 16,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  imageTop: {
    width: 325,
    height: 180,
    resizeMode: 'cover',
  },
  container: {
    alignItems: 'center',
    backgroundColor: '#282828',
  },
  title: {
    color: 'white',
    fontSize: 24,
  },
});