import React from 'react';
import { View, Image, Text, ScrollView, ImageBackground, TouchableOpacity, StyleSheet} from 'react-native';
import { SafeAreaView, SafeAreaProvider } from 'react-native-safe-area-context';
import Header from '../../components/Header';
import { useRouter } from 'expo-router';

const CARD_WIDTH = 120;
const CARD_HEIGHT = 100;

export default function HomeScreen() {
  const router = useRouter();

  const cards = Array.from({ length: 6 }, (_, i) => (
  <View key={i} style={styles.card}>
    {i === 0 ? (
      <>
        <Image
          source={require('@/assets/images/kash_logo.png')}
          style={styles.logo}
          resizeMode="contain"
        />
      </>
      ) : (
        <Text style={styles.cardText}>Become a Sponsor</Text>
      )}
    </View>
  ));

  const cardSponsors = Array.from({ length: 6 }, (_, i) => (
  <View key={i} style={styles.card}>
    <Text style={styles.cardText}>Become a Sponsor</Text>
  </View>
  ));

  return (
    <SafeAreaProvider>
          <Header />
      <SafeAreaView style={styles.container} >
        <ScrollView>
            <ImageBackground
              source={require('@/assets/images/destroyed_city.jpg')}
              style={styles.background}
              resizeMode="cover"
            >
              <View style={styles.textContainer}>
                <Text style={styles.date}>August 27–28, 2025</Text>
                <Text style={styles.location}>Orange County Convention Center, Orlando, FL</Text>
                <Text style={styles.title}>Anti-tradeshow</Text>
                <Text style={styles.subtitle}>More ROI // No BS</Text>
                <Text style={styles.description}>
                  Real Transactions. No Gatekeepers. Built for Bold Brands.
                </Text>
                <TouchableOpacity
                  style={styles.joinNowButton}
                    onPress={() => router.push('/membership')}>
                  <Text style={styles.buttonText}>JOIN THE REVOLUTION</Text>
                </TouchableOpacity>
              </View>
            </ImageBackground>
          <View>
            <Text style={styles.description}>
              REAL Sales. REAL Orders.
            </Text>
            <Text style={styles.description}>NO More Getting Drowned Out by Big Brands!</Text>
            <Text style={styles.description}>Exclusive Education and Strategies on HOW TO WIN @ RRR!</Text>
            <Text style={styles.RedTitle}>
              Event Details
            </Text>
            <View style={styles.row}>
              <View style={styles.col}>
                <Text style={styles.DesTitleRed}>Date :</Text>
              </View>
              <View style={styles.col}>
                <Text style={styles.DesTitleWhite}>August 27-28, 2025</Text>
              </View>
            </View>
            <View style={styles.row}>
              <View style={styles.col}>
                <Text style={styles.DesTitleRed}>Show Venue :</Text>
              </View>
              <View style={styles.col}>
                <Text style={styles.DesTitleWhite}>Orange County Convention Center, Orlando, FL</Text>
              </View>
            </View>
            <View style={styles.row}>
              <View style={styles.col}>
                <Text style={styles.DesTitleRed}>Mission :</Text>
              </View>
              <View style={styles.col}>
                <Text style={styles.DesTitleWhite}>To challenge outdated trade show models by providing real value, networking, and immediate ROI for brands, retailers, and investors.</Text>
              </View>
            </View>
            <TouchableOpacity style={styles.centerButton}>
              <Text style={styles.buttonText}>Join The Revolution</Text>
            </TouchableOpacity>
            <View style={styles.whiteBox}>
              <Text style={styles.boxHeading}>Register as an Exhibitor</Text>
                <Text style={styles.boxText}>Showcase your brand, products, and services to a dynamic audience.</Text>
              <View style={styles.bulletsContainer}>
                <Text style={styles.bulletPoint}>{'\u2022'} Gain visibility and attract potential clients</Text>
                <Text style={styles.bulletPoint}>{'\u2022'} Network with industry leaders and decision-makers.</Text>
                <Text style={styles.bulletPoint}>{'\u2022'} Drive business growth with exclusive exhibitor benefits.</Text>
              </View>
              <TouchableOpacity style={styles.centerButtonRed}>
                <Text style={styles.buttonText}>Register</Text>
              </TouchableOpacity>
            </View>
            <View style={styles.redBox}>
              <Text style={styles.redBoxHeading}>Join as an Attendee</Text>
              <Text style={styles.redBoxText}>Explore, engage, and expand your knowledge with like-minded professionals.</Text>
              <View style={styles.redBulletsContainer}>
                <Text style={styles.redBulletPoint}>{'\u2022'} Attend insightful sessions and workshops.</Text>
                <Text style={styles.redBulletPoint}>{'\u2022'} Connect with exhibitors and industry experts.</Text>
                <Text style={styles.redBulletPoint}>{'\u2022'} Discover the latest trends and innovations.</Text>
              </View>
              <TouchableOpacity style={styles.centerButtonWhite}>
                <Text style={styles.buttonTextRed}>Join Us</Text>
              </TouchableOpacity>
            </View>
            <View style={styles.whiteBox}>
              <Text style={styles.boxHeading}>Become a Member</Text>
                <Text style={styles.boxText}>Unlock premium benefits and stay ahead in the industry.</Text>
              <View style={styles.bulletsContainer}>
                <Text style={styles.bulletPoint}>{'\u2022'} Access exclusive resources and networking events.</Text>
                <Text style={styles.bulletPoint}>{'\u2022'} Get early-bird discounts for future conferences.</Text>
                <Text style={styles.bulletPoint}>{'\u2022'} Be part of a thriving community of professionals.</Text>
              </View>
              <TouchableOpacity style={styles.centerButtonRed}>
                <Text style={styles.buttonText}>Join Membership</Text>
              </TouchableOpacity>
            </View>
            <View >
              <Text style={styles.Heading}>EXPLORE THE ORLANDO</Text>
              <Text style={styles.Heading}>CONVENTION CENTER</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/map.png')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'flex-end', marginVertical: 20 }}>
              <Text style={styles.Heading}>MORE REVOLUTIONARY</Text>
              <Text style={styles.Heading}>UPDATES COMING</Text>
              <Text style={styles.Heading}>SOON...</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/ORLANDO.png')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.Heading}>EVENT SCHEDULE</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/event_schedule.jpg')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.redBoxHeading}>AUG 26TH, 2025</Text>
              <Text style={styles.Heading}>PRE-SHOW EVENT</Text>
              <Text style={styles.redBoxHeading}>Become a potential and professional freelancer</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/event_schedule.jpg')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.redBoxHeading}>AUG 27 & 28, 2025</Text>
              <Text style={styles.Heading}>ANTI-TRADE SHOW - </Text>
              <Text style={styles.Heading}>MAIN EVENT</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/event_schedule.jpg')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.redBoxHeading}>AUG 27 & 28, 2025</Text>
              <Text style={styles.Heading}>1 ON 1 WITH EXHIBITORS</Text>
              <Text style={styles.redBoxHeading}>Become a potential and professional freelancer</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/event_schedule.jpg')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.redBoxHeading}>AUG 27 & 28, 2025</Text>
              <Text style={styles.Heading}>EDUCATION SERIES</Text>
              <Text style={styles.redBoxHeading}>Explore knowledge from the outside world</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/event_schedule.jpg')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.redBoxHeading}>AUG 27 & 28, 2025</Text>
              <Text style={styles.Heading}> COMING SOON</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Image
                source={require('@/assets/images/event_schedule.jpg')}
                style={styles.image}
              />
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.redBoxHeading}>AUG 27 & 28, 2025</Text>
              <Text style={styles.Heading}> COMING SOON</Text>
            </View>
            <View style={{ alignItems: 'center', marginVertical: 20 }}>
              <Text style={styles.Heading}>SPONSORS</Text>
            </View>
            <ScrollView horizontal showsHorizontalScrollIndicator={false}>
              <View style={styles.scrollContainer}>
                {cards}
              </View>
            </ScrollView>
            <ScrollView horizontal showsHorizontalScrollIndicator={false}>
              <View style={styles.scrollContainer}>
                {cardSponsors}
              </View>
            </ScrollView>
          </View>
        </ScrollView>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  logo: {
    width: 80,
    height: 80,
  },
  scrollContainer: {
    flexDirection: 'row',
    paddingHorizontal: 16,
    gap: 12,
    marginBottom: 20,
  },
  card: {
    width: CARD_WIDTH,
    height: CARD_HEIGHT,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 10,
  },
  cardText: {
    fontSize: 13,
    color: '#000000',
    fontWeight: 'bold',
  },
  image: {
    width: 350,
    height: 200,
  },
  Heading: {
    fontSize: 30,
    fontWeight: 'bold',
    color: '#fff',
  },
  redBox: {
    backgroundColor: '#651613',
    borderRadius: 8,
    paddingHorizontal: 20,
    paddingVertical: 25,
    margin: 20,
    alignSelf: 'center',
    width: '90%',
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  redBoxText: {
    fontSize: 14,
    color: '#fff',
    marginBottom: 8,
  },
  redBoxHeading: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginVertical: 12,
    color: '#fff',
  },
  redBulletsContainer: {
    paddingLeft: 10,
  },
  redBulletPoint: {
    fontSize: 14,
    color: '#fff',
    marginBottom: 6,
  },
  whiteBox: {
    backgroundColor: '#fff',
    borderRadius: 8,
    paddingHorizontal: 20,
    paddingVertical: 25,
    margin: 20,
    alignSelf: 'center',
    width: '90%',
    elevation: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
  },
  boxText: {
    fontSize: 14,
    color: '#651613',
    marginBottom: 8,
  },
  boxHeading: {
    fontSize: 18,
    fontWeight: '600',
    textAlign: 'center',
    marginVertical: 12,
    color: '#651613',
  },
  bulletsContainer: {
    paddingLeft: 10,
  },
  bulletPoint: {
    fontSize: 14,
    color: '#651613',
    marginBottom: 6,
  },
  centerButtonWhite: {
    marginTop: 20,
    alignSelf: 'center',
    backgroundColor: '#fff',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 15,
  },
  centerButtonRed: {
    marginTop: 20,
    alignSelf: 'center',
    backgroundColor: '#651613',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 15,
  },
  centerButton: {
    marginTop: 20,
    alignSelf: 'center',
    backgroundColor: '#F02121',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 25,
  },
  DesTitleWhite: {
    fontSize: 15,
    marginTop: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  DesTitleRed: {
    fontSize: 15,
    marginTop: 20,
    fontWeight: 'bold',
    color: '#F02121',
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  col: {
    flex: 1,
    paddingHorizontal: 5,
  },
  container: {
    flex: 1,
    alignItems: 'center',
    paddingHorizontal: 20,
    backgroundColor: '#282828',
  },
  joinNowButton: {
    position: 'absolute',
    bottom: 20,
    right: 20,
    backgroundColor: '#000',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
  },
  buttonTextRed: {
    color: '#651613',
    fontWeight: 'bold',
    fontSize: 16,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 16,
  },
  overlay: {
    position: 'absolute',
    top: 0,
    bottom: 0,
    left: 0,
    right: 0,
    backgroundColor: 'rgba(0,0,0,0.5)',
    zIndex: 999,
  },
  sideMenu: {
    position: 'absolute',
    top: 0,
    bottom: 0,
    backgroundColor: '#222',
    paddingVertical: 60,
    paddingHorizontal: 20,
    zIndex: 1000,
  },
  menuItem: {
    color: '#fff',
    fontSize: 18,
    marginBottom: 20,
  },
  background: {
    width: '100%',
    height: 250,
    justifyContent: 'flex-start',
    position: 'relative',
    borderRadius: 20,
    overflow: 'hidden',
  },
  textContainer: {
    flex: 1,
    justifyContent: 'flex-end',
    paddingHorizontal: 20,
    paddingBottom: 30,
  },
  date: {
    color: '#fff',
    fontSize: 16,
  },
  location: {
    color: '#ccc',
    fontSize: 14,
    marginBottom: 12,
  },
  RedTitle: {
    fontSize: 35,
    marginTop: 20,
    fontWeight: 'bold',
    color: '#F02121',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
  },
  subtitle: {
    fontSize: 18,
    color: '#f0f0f0',
    marginVertical: 8,
  },
  description: {
    fontSize: 14,
    color: '#bbb',
    marginTop: 10,
  },
  button: {
    marginTop: 20,
    alignSelf: 'center',
    backgroundColor: '#ff4c4c',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 8,
  },
});