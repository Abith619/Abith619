import api from './api';

export const loginUser = async (email: string, password: string) => {
  try {
    const response = await api.post('/web/session/authenticate', {
      params: {
        db: 'rrr-mobile',
        login: email,
        password: password,
      },
    });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getUserDetails = async (userId: number) => {
  try {
    const response = await api.post('/web/dataset/call_kw', {
      params: {
        model: 'res.users',
        method: 'read',
        args: [[userId], ['name', 'login', 'image_1920', 'id']],
        kwargs: {},
      },
    });

    console.log('getUserDetails response:', response.data);

    const result = response.data?.result;

    if (!result || !Array.isArray(result) || result.length === 0) {
      console.error('Invalid user fetch result:', result);
      return null;
    }

    const userData = result[0];

    if (userData.image_1920) {
      userData.image = `data:image/png;base64,${userData.image_1920}`;
    }

    return userData;
  } catch (error) {
    console.error('Failed to fetch user details:', error);
    return null;
  }
};


