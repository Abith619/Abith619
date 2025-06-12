import React, { useRef, useEffect } from 'react';
import { View, Text, StyleSheet, Image, ScrollView, TouchableOpacity, Animated } from 'react-native';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { Table, TableWrapper, Row } from 'react-native-table-component';
import Header from '../../components/Header';

const speakerData = [
  { speaker: 'John Doe', date: 'August 15, 2025', time: '10:00 AM', location: 'Main Hall', duration: '1 hour' },
  { speaker: 'Jane Smith', date: 'August 16, 2025', time: '11:00 AM', location: 'Main Hall', duration: '1 hour' },
  { speaker: 'Alice Johnson', date: 'August 17, 2025', time: '1:00 PM', location: 'Main Hall', duration: '1 hour' },
  { speaker: 'Robert Brown', date: 'August 18, 2025', time: '2:00 PM', location: 'Main Hall', duration: '1 hour' },
];

export default function Agenda() {
  return (
    <SafeAreaProvider>
      <Header />
      <ScrollView>
        <View style={styles.container}>
          <Image
            source={require('@/assets/images/membership.png')}
            resizeMode="cover"
            style={styles.image}
          />
        <View style={styles.tableContainer}>
            <Table borderStyle={styles.tableBorder}>
                <Row
                    data={['Date', 'Details']}
                    style={styles.head}
                    textStyle={styles.headText}
                />
                {speakerData.map((item, index) => (
                    <AnimatedRow key={index} item={item} delay={index * 200} />
                ))}
            </Table>
        </View>
        </View>
      </ScrollView>
    </SafeAreaProvider>
  );
}

type SpeakerItem = {
  speaker: string;
  date: string;
  time: string;
  location: string;
  duration: string;
};

type AnimatedRowProps = {
  item: SpeakerItem;
  delay: number;
};

function AnimatedRow({ item, delay }: AnimatedRowProps) {
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 500,
      delay,
      useNativeDriver: true,
    }).start();
  }, [fadeAnim, delay]);

  // const handlePress = () => {
  //   Alert.alert('Agenda Details', `${item.speaker}\n${item.date} at ${item.time}\n${item.location}\n${item.duration}`);
  // };

  return (
    <Animated.View style={{ opacity: fadeAnim }}>
      <TouchableOpacity >
        <TableWrapper style={styles.tableRow}>
          <View style={styles.dateCell}>
            <Text style={styles.text}>{item.date}</Text>
            <Text style={styles.timeText}>{item.time}</Text>
          </View>
          <View style={styles.detailCell}>
            <Text style={styles.text}>Speaker: {item.speaker}</Text>
            <Text style={styles.text}>Location: {item.location}</Text>
            <Text style={styles.text}>Duration: {item.duration}</Text>

            <View style={styles.imageRow}>
              {[1, 2, 3, 4].map((num) => (
                <Image
                  key={num}
                  source={require('@/assets/images/speaker_placeholder.jpg')}
                  style={styles.speakerImage}
                />
              ))}
            </View>
          </View>
        </TableWrapper>
      </TouchableOpacity>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  imageRow: {
    flexDirection: 'row',
    marginTop: 5,
    gap: 10,
  },
  speakerImage: {
    width: 30,
    height: 30,
    borderRadius: 15,
    borderWidth: 1,
    borderColor: '#fff',
  },
  timeText: {
      fontSize: 12,
      color: '#aaa',
      marginTop: 2,
      },
  container: {
      flex: 1,
      alignItems: 'center',
      paddingTop: 20,
      backgroundColor: '#282828',
  },
  image: {
      marginBottom: 20,
  },
  tableContainer: {
      width: '90%',
      backgroundColor: '#282828',
      borderRadius: 10,
      overflow: 'hidden',
  },
  tableBorder: {
      borderWidth: 1,
      borderColor: '#ccc',
  },
  head: {
      height: 40,
      backgroundColor: '#282828',
  },
  headText: {
      margin: 6,
      fontWeight: 'bold',
      color: '#fff',
      textAlign: 'center',
  },
  tableRow: {
      flexDirection: 'row',
      borderBottomWidth: 1,
      borderBottomColor: '#ccc',
      paddingVertical: 10,
      paddingHorizontal: 5,
  },
  dateCell: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      borderRightWidth: 1,
      borderRightColor: '#ccc',
  },
  detailCell: {
      flex: 2,
      justifyContent: 'center',
      paddingLeft: 10,
  },
  text: {
      fontSize: 14,
      color: '#fff',
      marginBottom: 2,
  },
});