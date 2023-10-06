import { OHIF } from 'ohif-viewer'

const config = {
    servers: {
        dicomWeb: [
            {
                name: 'DCM4CHEE',
                wadoUriRoot: 'https://yourserver/dcm4chee-arc/aets/DCM4CHEE/wado',
                qidoRoot: 'https://yourserver/dcm4chee-arc/aets/DCM4CHEE/rs',
                wadoRoot: 'https://yourserver/dcm4chee-arc/aets/DCM4CHEE/rs',
                qidoSupportsIncludeField: true,
                imageRendering: 'wadors',
                thumbnailRendering: 'wadors',
            },
        ],
    },
    layout: {
        viewports: {
            left: {
                default: {
                    magnification: 1,
                    navigation: {
                        stackScroll: 'horizontal',
                    },
                },
            },
        },
    },
};
