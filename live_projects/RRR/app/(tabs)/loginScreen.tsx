import api from '@/components/api';
import { getUserDetails, loginUser } from '@/components/authService';
import { Ionicons } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { router } from 'expo-router';
import React, { useState } from 'react';
import { View, ImageBackground, KeyboardAvoidingView, Platform, StyleSheet, Text, TextInput, TouchableOpacity } from 'react-native';
import { useUser } from '../../components/UserContext';

const LoginScreen: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { setUser } = useUser();

  const handleLogin = async () => {
  try {
    const response = await loginUser(email, password);
    console.log('Login response:', response);

    if (response.result && response.result.uid) {
      const sessionId = response.result?.uid.toString();
      console.log('Session ID:', response.result.uid.toString());

      if (sessionId) {
        await AsyncStorage.setItem('session_id', sessionId);
        api.defaults.headers.Cookie = `session_id=${sessionId}`;
      }

      const userId = response.result.uid;
      const user = await getUserDetails(userId);
      console.log('User details:', user);

      if (user) {
        await AsyncStorage.setItem('user_info', JSON.stringify(user));
        setUser(user);
        alert(user.name + ' logged in successfully');
      }

      router.replace('/');
    } else {
      await AsyncStorage.removeItem('session_id');
      await AsyncStorage.removeItem('user_info');
      alert('Invalid credentials');
    }
  } catch (err) {
    console.error('Login error:', err);
    alert('Login failed');
  }
};

  return (
    <ImageBackground
      source={require('../../assets/images/login_bg_t.png')}
      style={styles.background}
      resizeMode="cover"
    >
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        style={styles.overlay}
      >
        <TouchableOpacity style={styles.backButton} onPress={() => router.replace('/login')}>
            <Ionicons name="arrow-back" size={24} color="#fff" />
        </TouchableOpacity>

        <Text style={styles.title}>Your Gateway to Retail Innovation</Text>

        <TextInput
          style={styles.input}
          placeholder="Email"
          placeholderTextColor="#ccc"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
          autoCapitalize="none"
        />

        <TextInput
          style={styles.input}
          placeholder="Password"
          placeholderTextColor="#ccc"
          value={password}
          onChangeText={setPassword}
          secureTextEntry
        />

      <View style={{ alignItems: 'flex-end', width: '100%' }}>
        <TouchableOpacity onPress={() => router.replace('/ForgotPasswordScreen')}>
          <Text style={styles.forgotText}>Forgot Password?</Text>
        </TouchableOpacity>
      </View>

      <TouchableOpacity onPress={handleLogin} style={styles.button}>
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>

      <View style={{ width: '100%' }}>
        <TouchableOpacity onPress={() => router.replace('/signUp')}>
          <Text style={styles.signupText}>don&apos;t have an account? Sign Up</Text>
        </TouchableOpacity>
      </View>

      </KeyboardAvoidingView>
    </ImageBackground>
  );
};

const styles = StyleSheet.create({
  signupText: {
    color: '#fff',
    fontSize: 14,
    textAlign: 'center',
    marginTop: 10,
  },
  backButton: {
    position: 'absolute',
    top: 50,
    left: 20,
    zIndex: 1,
  },
  forgotText: {
    color: '#fff',
    fontSize: 14,
    textAlign: 'right',
    marginBottom: 5,
  },
  background: {
    flex: 1,
  },
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 24,
  },
  title: {
    textAlign: "center",
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
    width: "100%",
    borderRadius: 10,
    marginTop: 10,
  },
  buttonText: {
    textAlign: "center",
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default LoginScreen;
