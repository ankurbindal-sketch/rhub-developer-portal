// @ts-check
// RHUB Developer Portal 1.0 — Docusaurus 3.x configuration

const {themes} = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'RHUB Developer Portal',
  tagline: 'Integration documentation for the RemittancesHub cross-border payment APIs',
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
      items: [
        {type: 'docSidebar', sidebarId: 'docsSidebar', position: 'left', label: 'Documentation'},
        {to: '/docs/api-index', label: 'API index', position: 'left'},
        {to: '/docs/master-apis', label: 'Master APIs', position: 'left'},
        {to: '/docs/errors', label: 'Errors', position: 'left'},
        {
          href: 'https://github.com/ankurbindal-sketch/rhub-developer-portal',
          label: 'GitHub',
          position: 'right',
        },
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
            {label: 'Source coverage notes', to: '/docs/appendix/source-notes'},
          ],
        },
        {
          title: 'About',
          items: [
            {label: 'Licence and source version', to: '/docs/appendix/licence'},
            {label: 'RemittancesHub', href: 'https://www.remittanceshub.com/'},
            {
              label: 'Repository',
              href: 'https://github.com/ankurbindal-sketch/rhub-developer-portal',
            },
          ],
        },
      ],
      copyright:
        'RemittancesHub holds the entire intellectual property rights of the source documentation. ' +
        'RHUB Developer Portal 1.0 — content migrated from the authoritative RHUB documentation source (Version 2.3.0).',
    },
    prism: {
      theme: themes.github,
      darkTheme: themes.vsDark,
      additionalLanguages: ['json', 'bash', 'http', 'java', 'csharp'],
    },
  }),
};

module.exports = config;
