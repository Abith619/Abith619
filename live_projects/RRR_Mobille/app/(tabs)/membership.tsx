import React from 'react';
import Header from '../../components/Header';
import { View, Text, StyleSheet, Image, ImageBackground, TouchableOpacity, ScrollView } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';

export default function Membership() {
    return (
        <SafeAreaProvider>
            <Header />
            <ScrollView>
            <View style={styles.container}>
                <Image
                    source={require('@/assets/images/membership.png')}
                    resizeMode="cover"
                />
                <Text style={styles.heading}>MEMBERSHIP PERKS</Text>

                <ImageBackground
                    source={require('@/assets/images/membership_back_img.png')}
                    resizeMode="cover"
                    style={styles.backgroundImage}
                >
                    <View style={styles.whiteBox}>
                        <Text style={styles.whiteBoxHeadingText}>MEMBERSHIP PERKS</Text>
                        <Text style={styles.whiteBoxText}>FIRST-YEAR INTRODUCTORY MEMBERSHIP FEE</Text>
                        <View style={styles.priceRow}>
                        <Text style={styles.whiteBoxPrice}>$298/</Text>
                        <Text style={styles.usdText}>USD</Text>
                    </View>
                        <View style={styles.bulletContainer}>
                            <Text style={styles.bulletTitle}>MEMBERS GAIN ACCESS TO</Text>

                            <View style={styles.bulletRow}>
                                <Ionicons name="checkmark" size={14} color="#651613" />
                                <Text style={styles.bulletPoint}>7.7% DISCOUNT ON TRADE SHOW BOOTH FEES</Text>
                            </View>

                            <View style={styles.bulletRow}>
                                <Ionicons name="checkmark" size={14} color="#651613" />
                                <Text style={styles.bulletPoint}>
                                EXCLUSIVE ACCESS TO INDUSTRY RESEARCH, EDUCATIONAL RESOURCES, AND EXPERT-LED WEBINARS
                                </Text>
                            </View>

                            <View style={styles.bulletRow}>
                                <Ionicons name="checkmark" size={14} color="#651613" />
                                <Text style={styles.bulletPoint}>PRIVATE NETWORKING EVENTS & MASTERMIND GROUPS</Text>
                            </View>

                            <View style={styles.bulletRow}>
                                <Ionicons name="checkmark" size={14} color="#651613" />
                                <Text style={styles.bulletPoint}>SPECIAL VENDOR AND SERVICE PROVIDER DISCOUNT</Text>
                            </View>

                            <View style={styles.bulletRow}>
                                <Ionicons name="checkmark" size={14} color="#651613" />
                                <Text style={styles.bulletPoint}>PRIORITY ACCESS & DISCOUNTED RATES FOR ADDITIONAL RRR EVENTS</Text>
                            </View>
                            <View style={styles.underline} />
                            <View style={styles.priceRow}>
                                <Text style={styles.price}>$298/</Text>
                                <Text style={styles.priceSub}>USD (Annually)</Text>
                            </View>

                            <TouchableOpacity style={styles.button}>
                                <Text style={styles.buttonText}>Discover</Text>
                            </TouchableOpacity>
                        </View>
                    </View>
                </ImageBackground>
            </View>
        </ScrollView>
    </SafeAreaProvider>
    );
}

const styles = StyleSheet.create({
    price: {
        fontSize: 50,
        fontWeight: 'bold',
        color: '#651613',
    },
    priceSub: {
        fontSize: 20,
        color: '#b0a9a9',
        marginLeft: 8,
        marginBottom: 8,
    },
    button: {
        backgroundColor: '#651613',
        paddingVertical: 12,
        paddingHorizontal: 40,
        borderRadius: 6,
        marginTop: 20,
    },
    buttonText: {
        color: '#fff',
        textAlign: 'center',
        fontWeight: 'bold',
        fontSize: 16,
    },
    underline: {
        borderBottomColor: '#651613',
        borderBottomWidth: 2,
        marginTop: 8,
        width: '80%',
        alignSelf: 'center',
    },
    bulletContainer: {
        width: '100%',
        paddingHorizontal: 10,
        marginTop: 10,
    },
    bulletTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
        textAlign: 'center',
    },
    bulletRow: {
        flexDirection: 'row',
        alignItems: 'flex-start',
        marginBottom: 6,
    },
    bulletPoint: {
        fontSize: 12,
        color: '#000',
        fontWeight: 'bold',
        marginLeft: 6,
        flex: 1,
        textTransform: 'uppercase',
    },
    priceRow: {
        flexDirection: 'row',
        alignItems: 'flex-end',
        justifyContent: 'center',
        marginTop: 10,
    },
    usdText: {
        fontSize: 20,
        marginLeft: 4,
        marginBottom: 6,
        fontWeight: 'bold',
    },
    benefitTitle: {
        fontSize: 20,
        fontWeight: 'bold',
        marginTop: 20,
        marginBottom: 10,
    },
    bulletList: {
        alignSelf: 'flex-start',
    },
    whiteBoxPrice: {
        fontSize: 50,
        fontWeight: 'bold',
    },
    whiteBoxText: {
        fontSize: 12,
        fontWeight: 'bold',
        textAlign: 'center',
    },
    container: {
        flex: 1,
        alignItems: 'center',
        paddingTop: 20,
        backgroundColor: '#282828',
    },
    heading: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#fff',
        marginVertical: 20,
    },
    backgroundImage: {
        width: '100%',
        justifyContent: 'center',
        alignItems: 'center',
    },
    whiteBox: {
        backgroundColor: '#fff',
        padding: 20,
        borderRadius: 10,
        width: '90%',
        shadowColor: '#000',
        shadowOpacity: 0.1,
        shadowOffset: { width: 0, height: 2 },
        shadowRadius: 5,
        elevation: 5,
        alignItems: 'center',
    },
    whiteBoxHeadingText: {
        fontSize: 24,
        fontWeight: 'bold',
        color: '#651613',
        textAlign: 'center',
    },
});
