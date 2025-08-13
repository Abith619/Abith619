import { Slot } from 'expo-router';
import { CartProvider } from '../../components/CartContext';

export default function Layout() {
  return (
    <CartProvider>
      <Slot />
    </CartProvider>
  );
}
