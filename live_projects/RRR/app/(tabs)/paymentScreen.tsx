import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image, ScrollView } from 'react-native';
import * as Animatable from 'react-native-animatable';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

export default function PaymentScreen() {
  const [selectedMethod, setSelectedMethod] = useState('paypal');

  const product = { name: 'Premium Product', price: 150 };
  const tax = 15;
  const total = product.price + tax;

  const handlePayment = () => {
    console.log('Processing payment...');
  };

  return (
    <View style={styles.screen}>
      <Header />

      <ScrollView contentContainerStyle={styles.container}>

        <Animatable.View animation="fadeInUp" duration={800} style={styles.card}>
          <Text style={styles.title}>Order Summary</Text>
          <View style={styles.row}>
            <Text style={styles.label}>Product:</Text>
            <Text style={styles.value}>${product.price.toFixed(2)}</Text>
          </View>
          <View style={styles.row}>
            <Text style={styles.label}>Tax:</Text>
            <Text style={styles.value}>${tax.toFixed(2)}</Text>
          </View>
          <View style={styles.row}>
            <Text style={styles.totalLabel}>Total:</Text>
            <Text style={styles.totalValue}>${total.toFixed(2)}</Text>
          </View>
        </Animatable.View>

        <Animatable.View animation="fadeInUp" delay={300} duration={800} style={styles.card}>
          <Text style={styles.title}>Select Payment Method</Text>

          <TouchableOpacity
            style={[
              styles.paymentOption,
              selectedMethod === 'paypal' && styles.selectedOption,
            ]}
            onPress={() => setSelectedMethod('paypal')}
          >
            <Image
              source={require('@/assets/images/paypal_logo.png')}
              style={styles.paymentIcon}
            />
            <Text style={styles.paymentText}>Pay with PayPal</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[
              styles.paymentOption,
              selectedMethod === 'card' && styles.selectedOption,
            ]}
            onPress={() => setSelectedMethod('card')}
          >
            <Image
              source={require('@/assets/images/card.webp')}
              style={styles.paymentIcon}
            />
            <Text style={styles.paymentText}>Credit/Debit Card</Text>
          </TouchableOpacity>
        </Animatable.View>

        <Animatable.View animation="fadeInUp" delay={500} duration={800}>
          <TouchableOpacity style={styles.payButton} onPress={handlePayment}>
            <Text style={styles.payButtonText}>Make Payment</Text>
          </TouchableOpacity>
        </Animatable.View>

      </ScrollView>

      <Footer />
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    backgroundColor: '#282828',
  },
  container: {
    padding: 20,
    paddingBottom: 100,
  },
  card: {
    backgroundColor: '#3a3a3a',
    borderRadius: 12,
    padding: 20,
    marginBottom: 20,
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 6,
    elevation: 5,
  },
  title: {
    fontSize: 18,
    color: '#fff',
    marginBottom: 15,
    fontWeight: 'bold',
  },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginVertical: 8,
  },
  label: {
    color: '#ccc',
    fontSize: 16,
  },
  value: {
    color: '#ccc',
    fontSize: 16,
  },
  totalLabel: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  totalValue: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
  },
  paymentOption: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#444',
    padding: 15,
    borderRadius: 10,
    marginVertical: 10,
  },
  selectedOption: {
    borderWidth: 2,
    borderColor: '#651613',
  },
  paymentIcon: {
    width: 32,
    height: 32,
    marginRight: 10,
    resizeMode: 'contain',
  },
  paymentText: {
    color: '#fff',
    fontSize: 16,
  },
  payButton: {
    backgroundColor: '#651613',
    paddingVertical: 15,
    borderRadius: 10,
    alignItems: 'center',
  },
  payButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});
