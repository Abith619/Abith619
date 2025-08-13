import React, { useState } from 'react';
import { View, Text, StyleSheet, ImageBackground, TextInput, TouchableOpacity, KeyboardAvoidingView, Platform, Alert } from 'react-native';
import { router } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

const ForgotPasswordScreen: React.FC = () => {
  const [email, setEmail] = useState('');
  const [otp, setOtp] = useState('');

  const handleSubmit = () => {
    Alert.alert('Password Reset', `Password reset OTP verified for ${email}`);
  };

  const handleGetOtp = () => {
    if (!email) {
      Alert.alert('Error', 'Please enter your email.');
    } else {
      Alert.alert('OTP Sent', `OTP sent to ${email}`);
    }
  };

  return (
    <ImageBackground
      source={require('../../assets/images/login_bg_t.png')}
      style={styles.background}
      resizeMode="cover"
    >
      <KeyboardAvoidingView
        style={styles.overlay}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        <TouchableOpacity style={styles.backButton} onPress={() => router.replace('/loginScreen')}>
          <Ionicons name="arrow-back" size={24} color="#fff" />
        </TouchableOpacity>

        <Text style={styles.heading}>Forgot Password</Text>

        <View style={styles.inputWithLink}>
          <TextInput
            style={styles.inputFlex}
            placeholder="Enter your email"
            placeholderTextColor="#ccc"
            value={email}
            onChangeText={setEmail}
            keyboardType="email-address"
            autoCapitalize="none"
          />
          <TouchableOpacity onPress={handleGetOtp}>
            <Text style={styles.getOtpText}>Get OTP</Text>
          </TouchableOpacity>
        </View>

        {/* OTP Input */}
        <TextInput
          style={styles.input}
          placeholder="Enter OTP"
          placeholderTextColor="#ccc"
          keyboardType="numeric"
          value={otp}
          onChangeText={setOtp}
        />

        <TouchableOpacity style={styles.button} onPress={handleSubmit}>
          <Text style={styles.buttonText}>Submit</Text>
        </TouchableOpacity>
      </KeyboardAvoidingView>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
    inputWithLink: {
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
        borderRadius: 10,
        marginBottom: 20,
        paddingHorizontal: 10,
    },
    inputFlex: {
        flex: 1,
        padding: 14,
        fontSize: 16,
        color: '#000',
    },
    getOtpText: {
        color: '#00BFFF',
        fontWeight: 'bold',
        fontSize: 14,
        paddingHorizontal: 10,
    },
    backButton: {
        position: 'absolute',
        top: 50,
        left: 20,
        zIndex: 1,
    },
    background: {
        flex: 1,
    },
    overlay: {
        flex: 1,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        justifyContent: 'center',
        alignItems: 'center',
        paddingHorizontal: 24,
    },
    heading: {
        fontSize: 28,
        color: '#fff',
        marginBottom: 40,
        fontWeight: 'bold',
    },
    input: {
        width: '100%',
        backgroundColor: '#313E55C7',
        padding: 14,
        borderRadius: 10,
        marginBottom: 20,
        color: '#000',
        fontSize: 16,
    },
    button: {
        backgroundColor: '#651613',
        paddingVertical: 14,
        paddingHorizontal: 60,
        borderRadius: 10,
    },
    buttonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
    },
});

export default ForgotPasswordScreen;
