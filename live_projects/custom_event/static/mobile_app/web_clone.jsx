import React from 'react';
import { SafeAreaView } from 'react-native';
import { WebView } from 'react-native-webview';

const App = () => {
  return (
    <SafeAreaView style={{ flex: 1 }}>
      <WebView source={{ uri: 'http://10.0.2.2:8069'}}
        javaScriptEnabled={true}
      />
    </SafeAreaView>
  );
};

export default App;