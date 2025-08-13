import React from 'react';
import { View, Image, StyleSheet, Text, ScrollView } from 'react-native';

const App = () => {
  return (
    <ScrollView style={styles.container}>
      <View style={styles.headerCard}>
        <Image
          source={require('./src/img/Card.png')} style={styles.headerImage}
        />
        <Image
          source={require('./src/img/logo_white.png')}
          style={styles.logoImage}
        />
        <Image
          source={require('./src/img/bell.png')}
          style={styles.cartImage}
        />
        <Image
          source={require('./src/img/hamburger.jpg')}
        />
      </View>

      <Text style={styles.revolutionText}>The Retail Revolution Starts Here</Text>

      <View style={styles.featuresContainer}>
        <Text style={styles.featureText}>Curated Buyer Interaction</Text>
        <Text style={styles.featureText}>REAL Sale. REAL Orders. Disruptive Experience-Based Selling</Text>
        <Text style={styles.featureText}>Exclusive Education and Strategies on HOW TO WIN</Text>
        <Text style={styles.featureText}>NO More Getting Drowned Out by Big Brands!</Text>
      </View>

      {/* Event Details */}
      <Text style={styles.sectionTitle}>Event Details</Text>
      <View style={styles.eventDetails}>
        <Text style={styles.detailLabel}>Date:</Text>
        <Text style={styles.detailValue}>August 27-28, 2025</Text>
        <Text style={styles.detailLabel}>Pre Show Party:</Text>
        <Text style={styles.detailValue}>August 26, 2025</Text>
        <Text style={styles.detailLabel}>Venue:</Text>
        <Text style={styles.detailValue}>Orange County Convention Center, Orlando, FL</Text>
        <Text style={styles.detailLabel}>Move-in Dates:</Text>
        <Text style={styles.detailValue}>August 26, 2025</Text>
        <Text style={styles.detailLabel}>Move-out Date:</Text>
        <Text style={styles.detailValue}>August 28, 2025</Text>
        <Text style={styles.detailLabel}>Mission:</Text>
        <Text style={styles.detailValue}>To challenge outdated trade show models by providing real value, networking, and immediate ROI for brands, retailers, and investors.</Text>
      </View>

      {/* Registration Cards */}
      <View style={styles.cardContainer}>
        <View style={styles.card}>
          <Text style={styles.cardTitle}>Register as an Exhibitor</Text>
          <Text style={styles.cardDescription}>
            Showcase your brand, products, and services to a dynamic audience.
            Gain visibility and attract potential clients.
            Network with industry leaders and decision-makers.
            Drive business growth with exclusive exhibitor benefits.
          </Text>
          <View style={styles.button}>
            <Text style={styles.buttonText}>Register</Text>
          </View>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>Join as an Attendee</Text>
          <Text style={styles.cardDescription}>
            Explore, engage, and expand your knowledge with like-minded professionals.
            Attend insightful sessions and workshops.
            Connect with exhibitors and industry experts.
            Discover the latest trends and innovations.
          </Text>
          <View style={styles.button}>
            <Text style={styles.buttonText}>Join Us</Text>
          </View>
        </View>

        <View style={styles.card}>
          <Text style={styles.cardTitle}>Become a Member</Text>
          <Text style={styles.cardDescription}>
            Unlock premium benefits and stay ahead in the industry.
            Access exclusive resources and networking events.
            Get early-bird discounts for future conferences.
            Be part of a thriving community of professionals.
          </Text>
          <View style={styles.button}>
            <Text style={styles.buttonText}>Join Membership</Text>
          </View>
        </View>
      </View>

      {/* Event Schedule */}
      <Text style={styles.sectionTitle}>EVENT SCHEDULE</Text>
      <View style={styles.scheduleContainer}>
        <View style={styles.scheduleItem}>
          <Image source={{ uri: 'https://placehold.co/330x214' }} style={styles.scheduleImage} />
          <Text style={styles.scheduleDate}>AUG 26TH, 2025</Text>
          <Text style={styles.scheduleTitle}>PRE-SHOW EVENT</Text>
          <Text style={styles.scheduleDescription}>Become a potential and professional freelancer</Text>
        </View>
        {/* Add more schedule items similarly */}
      </View>

      {/* Sponsors */}
      <Text style={styles.sectionTitle}>Sponsors</Text>
      <View style={styles.sponsorContainer}>
        <Image source={{ uri: 'https://placehold.co/87x35' }} style={styles.sponsorLogo} />
        <View style={styles.sponsorButton}>
          <Text style={styles.sponsorButtonText}>BECOME A SPONSOR</Text>
        </View>
        {/* Add more sponsor items */}
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'rgba(68, 68, 68, 0.27)',
  },
  headerCard: {
    width: '100%',
    height: 207,
    position: 'relative',
  },
  headerImage: {
    width: 361.9,
    height: 207,
    borderRadius: 14.08,
  },
  chainImage: {
    width: 269.86,
    height: 269.86,
    position: 'absolute',
    left: -6.7,
    top: 9.99,
    transform: [{ rotate: '-4deg' }],
  },
  antiTradeShowTag: {
    width: 107.55,
    height: 19.64,
    position: 'absolute',
    left: 216.52,
    top: 52.52,
    backgroundColor: '#651613',
    transform: [{ rotate: '-24deg' }],
  },
  antiTradeShowText: {
    color: 'white',
    fontSize: 15.94,
    fontFamily: 'Haettenschweiler',
    textTransform: 'uppercase',
  },
  roiTag: {
    width: 80.72,
    height: 15.28,
    position: 'absolute',
    left: 261.68,
    top: 65.99,
    backgroundColor: 'white',
    transform: [{ rotate: '-25deg' }],
  },
  roiText: {
    color: '#651613',
    fontSize: 12.4,
    fontFamily: 'Haettenschweiler',
    textTransform: 'uppercase',
  },
  logoImage: {
    width: 95.28,
    height: 64,
    position: 'absolute',
    left: 22,
    top: 40,
  },
  cartImage: {
    width: 79,
    height: 79,
    position: 'absolute',
    left: 289,
    top: 248,
  },
  revolutionText: {
    color: 'white',
    fontSize: 14.74,
    fontFamily: 'Reggae One',
    marginTop: 20,
    marginLeft: 34,
  },
  featuresContainer: {
    marginTop: 20,
    marginLeft: 21,
  },
  featureText: {
    color: 'white',
    fontSize: 10.65,
    fontFamily: 'Reggae One',
    marginBottom: 2,
  },
  sectionTitle: {
    color: '#A10909',
    fontSize: 23.21,
    fontFamily: 'Reggae One',
    marginTop: 20,
    marginLeft: 21,
  },
  eventDetails: {
    marginLeft: 21,
    marginTop: 10,
  },
  detailLabel: {
    color: '#A10909',
    fontSize: 14.76,
    fontFamily: 'Reggae One',
    marginBottom: 5,
  },
  detailValue: {
    color: 'white',
    fontSize: 14.76,
    fontFamily: 'Reggae One',
    marginLeft: 135,
    marginTop: -20,
    marginBottom: 15,
  },
  cardContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
  card: {
    width: 280,
    backgroundColor: 'white',
    padding: 17,
    marginBottom: 20,
    borderRadius: 10,
  },
  cardTitle: {
    color: '#651613',
    fontSize: 17.89,
    fontFamily: 'Reggae One',
    textAlign: 'center',
    marginBottom: 10,
  },
  cardDescription: {
    color: '#651613',
    fontSize: 11.18,
    fontFamily: 'Reggae One',
    opacity: 0.8,
    marginBottom: 10,
  },
  button: {
    backgroundColor: '#651613',
    padding: 10,
    borderRadius: 6,
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 13.42,
    fontFamily: 'Reggae One',
  },
  scheduleContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
  scheduleItem: {
    alignItems: 'center',
    marginBottom: 20,
  },
  scheduleImage: {
    width: 329.88,
    height: 213.98,
  },
  scheduleDate: {
    color: 'white',
    fontSize: 10.7,
    fontFamily: 'Inter',
    marginTop: 5,
  },
  scheduleTitle: {
    color: 'white',
    fontSize: 17.83,
    fontFamily: 'Inter',
    fontWeight: '700',
  },
  scheduleDescription: {
    color: 'white',
    fontSize: 10.7,
    fontFamily: 'Inter',
  },
  sponsorContainer: {
    marginTop: 20,
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
  },
  sponsorLogo: {
    width: 87.38,
    height: 34.58,
    margin: 10,
  },
  sponsorButton: {
    width: 114.2,
    height: 71,
    backgroundColor: 'white',
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: 9.93,
    margin: 10,
  },
  sponsorButtonText: {
    color: 'black',
    fontSize: 13.82,
    fontFamily: 'Reggae One',
    textAlign: 'center',
  },
});

export default App;