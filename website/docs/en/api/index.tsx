export const frontmatter = {
  pageType: 'custom',
};

import { RedocStandalone } from 'redoc';

const APIPage = () => {
  return (
    <RedocStandalone
      specUrl="/v1/openapi.json"
      options={{
        hideHostname: true,
        // nativeScrollbars: true,
        theme: { colors: { primary: { main: '#dd5522' } } },
      }}
    />
  );
};

export default APIPage;
