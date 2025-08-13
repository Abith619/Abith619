import { createStackNavigator } from '@react-navigation/stack';
import HomeScreen from '../app/(tabs)/index';
import AppLayout from './AppLayout';

const Stack = createStackNavigator();

export default function AppNavigator() {
  return (
    <Stack.Navigator
      screenOptions={{
        header: () => null,
      }}
    >
      <Stack.Screen name="Home">
        {() => (
          <AppLayout>
            <HomeScreen />
          </AppLayout>
        )}
      </Stack.Screen>
    </Stack.Navigator>
  );
}
