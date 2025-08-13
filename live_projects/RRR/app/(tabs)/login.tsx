import React from 'react';
import { View, Text, StyleSheet, ImageBackground, TouchableOpacity, Image } from 'react-native';
import { router } from 'expo-router';

const LoginScreen: React.FC = () => {
  return (
    <ImageBackground
      source={require('../../assets/images/login_bg_t.png')}
      style={styles.background}
      resizeMode="cover"
    >
      <View style={styles.overlay}>
        <Image
          source={require('@/assets/images/logo.png')}
          style={{...styles.logo, marginTop: 'auto'}}
          resizeMode="contain"
        />

        <TouchableOpacity style={{...styles.SignupButton, marginTop: 50}} onPress={() => router.replace('/signUp')}>
          <Text style={styles.DarkbuttonText}>Create Account</Text>
        </TouchableOpacity>

        <View style={styles.inlineText}>
          <Text style={styles.subText}>Already registered? </Text>
          <TouchableOpacity onPress={() => router.replace('/loginScreen')}>
            <Text style={styles.loginLink}>Log In</Text>
          </TouchableOpacity>
        </View>

        <TouchableOpacity style={{...styles.button, marginTop: 30}}>
          <Image
            source={require('../../assets/images/google.png')}
            style={styles.icon}
          />
          <Text style={styles.buttonText}>Sign in with Google</Text>
        </TouchableOpacity>

        <TouchableOpacity style={{...styles.button, marginBottom: 150}}>
          <Image
            source={require('../../assets/images/apple.png')}
            style={styles.icon}
          />
          <Text style={styles.buttonText}>Sign in with iCloud</Text>
        </TouchableOpacity>
      </View>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  logo: {
    width: 250,
    height: 250,
  },
  inlineText: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 12,
  },

  subText: {
    fontSize: 14,
    color: '#fff',
  },

  loginLink: {
    fontSize: 14,
    color: '#00BFFF',
    fontWeight: 'bold',
  },

  background: {
    flex: 1,
  },
  overlay: {
    flex: 1,
    // backgroundColor: 'rgba(40, 40, 40, 0.6)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  text: {
    fontSize: 28,
    color: '#fff',
    textAlign: 'center',
    marginBottom: 50,
    fontWeight: 'bold',
  },
  SignupButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#651613',
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 10,
    marginBottom: 15,
    width: '80%',
    justifyContent: 'center',
  },
  button: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#0F0F0F80',
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 10,
    marginBottom: 15,
    width: '80%',
    justifyContent: 'center',
  },
  buttonText: {
    fontSize: 16,
    marginLeft: 25,
    color: '#fff',
    fontWeight: '600',
  },
  DarkbuttonText: {
    fontSize: 16,
    color: '#fff',
    fontWeight: '600',
  },
  icon: {
    width: 24,
    height: 30,
  },
});

export default LoginScreen;
