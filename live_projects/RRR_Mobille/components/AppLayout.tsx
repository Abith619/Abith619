import React from 'react';
import { View } from 'react-native';
import Header from './Header';

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <View style={{ flex: 1 }}>
      <Header />
      {children}

    </View>
  );
}
