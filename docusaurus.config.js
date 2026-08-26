// @ts-check
// RHUB Developer Portal 1.0 — Docusaurus 3.x configuration

const {themes} = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'RHUB Developer Portal',
  tagline: 'Integration documentation for the RemittancesHub cross-border payment APIs',
  // The supplied RHUB asset is a wide wordmark (396x67, 5.9:1); it cannot serve as a
  // square favicon without cropping or padding it, so no favicon is configured and
  // none has been fabricated.
  favicon: undefined,

  url: 'https://ankurbindal-sketch.github.io',
  baseUrl: '/rhub-developer-portal/',
  trailingSlash: false,

  organizationName: 'ankurbindal-sketch',
  projectName: 'rhub-developer-portal',
  deploymentBranch: 'gh-pages',

  onBrokenLinks: 'throw',
  onBrokenAnchors: 'warn',
  onDuplicateRoutes: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  markdown: {
    mermaid: false,
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  headTags: [
    {
      tagName: 'link',
      attributes: {rel: 'preconnect', href: 'https://fonts.googleapis.com'},
    },
    {
      tagName: 'link',
      attributes: {rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: 'anonymous'},
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap',
      },
    },
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: 'docs',
          routeBasePath: 'docs',
          sidebarPath: require.resolve('./sidebars.js'),
          showLastUpdateTime: false,
          breadcrumbs: true,
          sidebarCollapsible: true,
        },
        blog: false,
        pages: {},
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
        },
      }),
    ],
  ],

  themes: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      /** @type {import('@easyops-cn/docusaurus-search-local').PluginOptions} */
      ({
        hashed: true,
        indexBlog: false,
        docsRouteBasePath: '/docs',
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        searchBarShortcutHint: false,
      }),
    ],
  ],

  themeConfig: /** @type {import('@docusaurus/preset-classic').ThemeConfig} */ ({
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    docs: {
      sidebar: {hideable: true, autoCollapseCategories: false},
    },
    tableOfContents: {minHeadingLevel: 2, maxHeadingLevel: 3},
    navbar: {
      title: 'RHUB Developer Portal',
      hideOnScroll: false,
      // Official RHUB asset, supplied by RHUB. 396x67 native; rendered at 28px height with
      // width scaled to match (165x28) so the aspect ratio is preserved exactly.
      logo: {
        alt: 'RemittancesHub — Cross Border Business Payments',
        src: 'img/rhub.png',
        width: 189,
        height: 32,
      },
      items: [
        // "Master APIs" was removed from the global navbar: the Master / reference API
        // section is already a top-level sidebar category and is listed in the API Index,
        // so a third entry point added clutter without adding a route. The pages and the
        // sidebar section are unchanged.
        {type: 'docSidebar', sidebarId: 'docsSidebar', position: 'left', label: 'Documentation'},
        {to: '/docs/api-index', label: 'API Index', position: 'left'},
        {to: '/docs/errors', label: 'Errors', position: 'left'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Start here',
          items: [
            {label: 'Overview', to: '/docs/'},
            {label: 'Integration flow', to: '/docs/getting-started/integration-flow'},
            {label: 'How to read this reference', to: '/docs/getting-started/conventions'},
          ],
        },
        {
          title: 'Core APIs',
          items: [
            {label: 'Authentication', to: '/docs/authentication/authentication'},
            {label: 'Quotation', to: '/docs/quotation/quotation'},
            {label: 'Payout', to: '/docs/payout/payout'},
            {label: 'Transaction Enquiry', to: '/docs/transactions/transaction-enquiry'},
          ],
        },
        {
          title: 'Reference',
          items: [
            {label: 'API index', to: '/docs/api-index'},
            {label: 'Master APIs', to: '/docs/master-apis'},
            {label: 'Errors and response codes', to: '/docs/errors'},
            {label: 'Validation rules', to: '/docs/validation/currency-validations'},
          ],
        },
        {
          title: 'About',
          items: [
            {label: 'Licence', to: '/docs/appendix/licence'},
            {label: 'RemittancesHub', href: 'https://www.remittanceshub.com/'},
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} RemittancesHub. All rights reserved.`,
    },
    prism: {
      theme: themes.github,
      darkTheme: themes.vsDark,
      additionalLanguages: ['json', 'bash', 'http', 'java', 'csharp'],
    },
  }),
};

module.exports = config;
