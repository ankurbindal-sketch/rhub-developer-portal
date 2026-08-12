// @ts-check
// Explicit navigation for RHUB Developer Portal 1.0.
// Order follows the integration journey documented in the RHUB source:
// authentication -> quotation -> payout -> transaction enquiry, then supporting APIs.

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Getting started',
      collapsed: false,
      items: [
        'getting-started/integration-flow',
        'getting-started/transaction-flows',
        'getting-started/conventions',
      ],
    },
    {
      type: 'category',
      label: 'API reference',
      collapsed: false,
      items: [
        'api-index',
        {
          type: 'category',
          label: 'Authentication',
          items: ['authentication/authentication'],
        },
        {
          type: 'category',
          label: 'Quotation',
          items: ['quotation/quotation'],
        },
        {
          type: 'category',
          label: 'Payout',
          items: ['payout/payout', 'payout/wpt-payout'],
        },
        {
          type: 'category',
          label: 'Transactions',
          items: ['transactions/transaction-enquiry'],
        },
        {
          type: 'category',
          label: 'Balance',
          items: ['balance/balance-enquiry'],
        },
        {
          type: 'category',
          label: 'Customers',
          items: ['customers/customer-registration'],
        },
        {
          type: 'category',
          label: 'Documents',
          items: ['documents/document-upload'],
        },
      ],
    },
    {
      type: 'category',
      label: 'Master / reference APIs',
      collapsed: true,
      link: {type: 'doc', id: 'master-apis/master-index'},
      items: [
        'master-apis/remittance-purpose',
        'master-apis/source-of-fund',
        'master-apis/relationship',
        'master-apis/document-id-type',
        'master-apis/occupation',
        'master-apis/business-type',
        'master-apis/business-registration-type',
        'master-apis/account-type',
        'master-apis/wpt-wallet-list',
        'master-apis/bank-list',
        'master-apis/customer-legal-status',
        'master-apis/nature-of-business',
        'master-apis/customer-occupation-type',
        'master-apis/customer-individual-document-type',
      ],
    },
    {
      type: 'category',
      label: 'Validation',
      collapsed: true,
      items: ['validation/currency-validations', 'validation/country-validations'],
    },
    {
      type: 'category',
      label: 'Errors and response codes',
      collapsed: true,
      link: {type: 'doc', id: 'errors/errors-index'},
      items: [
        'errors/current-error-codes',
        'errors/transaction-status-codes',
        'errors/error-codes',
      ],
    },
    {
      type: 'category',
      label: 'WPT integration set',
      collapsed: true,
      link: {type: 'doc', id: 'wpt/wpt-index'},
      items: ['wpt/customer-registration', 'wpt/quotation', 'wpt/payout'],
    },
    // Recovery / audit material is intentionally NOT exposed here.
    //
    // The following categories were removed from the public developer navigation and must
    // not be re-added: "Template management" (docs/template-management/*),
    // "Unlinked source pages" (docs/legacy/*), "Project reference"
    // (docs/appendix/source-notes, unpublished-master-apis, unpublished-apis, licence).
    //
    // The pages themselves are still generated and still ship in the repository for
    // auditability. tools/generate.py marks all of them `unlisted: true` (see
    // HIDDEN_FROM_PUBLIC_NAV there), which also keeps them out of site search and the
    // sitemap. The licence page stays public and is reachable from the footer.
  ],
};

module.exports = sidebars;
