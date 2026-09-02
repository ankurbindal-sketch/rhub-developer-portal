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
        'getting-started/environments',
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
      label: 'Virtual Accounts',
      collapsed: true,
      link: {type: 'doc', id: 'virtual-accounts/va-index'},
      items: [
        'virtual-accounts/integration-flow',
        'virtual-accounts/va-currencies',
        'virtual-accounts/document-requirements',
        'virtual-accounts/upload-documents',
        'virtual-accounts/get-documents',
        {
          type: 'category',
          label: 'Individual customer',
          items: [
            'virtual-accounts/individual/create',
            'virtual-accounts/individual/retrieve',
            'virtual-accounts/individual/edit',
          ],
        },
        {
          type: 'category',
          label: 'Business customer',
          items: [
            'virtual-accounts/business/create',
            'virtual-accounts/business/retrieve',
            'virtual-accounts/business/edit',
          ],
        },
        'virtual-accounts/va-request-status',
        'virtual-accounts/va-approval-process',
        'virtual-accounts/va-reference-data',
        'virtual-accounts/responses-and-errors',
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
      ],
    },
    // Recovery / audit material is intentionally NOT exposed here.
    //
    // The following categories were removed from the public developer navigation and must
    // not be re-added: "WPT integration set" (docs/wpt/*), the legacy HTTP/application error page
    // (docs/errors/error-codes), "Template management"
    // (docs/template-management/*),
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
