import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';

/*
 * Landing page for RHUB Developer Portal 1.0.
 *
 * Every factual statement here is taken from the authoritative RHUB source
 * export (README.md, apisequence.md, master.md, responseCodes.md). No product
 * claims, performance figures or capabilities have been added.
 */

const JOURNEY = [
  {
    index: '01',
    kind: 'Core transaction API',
    name: 'Authenticate',
    note: 'Obtain the access token every other call carries.',
    to: '/docs/authentication/authentication',
  },
  {
    index: '02',
    kind: 'Core transaction API',
    name: 'Quotation',
    note: 'Price the transaction. No registered customer needed: send an existing customerCode, or send it blank.',
    to: '/docs/quotation/quotation',
  },
  {
    index: '03',
    kind: 'Preparation',
    name: 'Documents',
    note: 'KYC/KYB for payout, plus invoice documentation for B2B, B2C and C2B.',
    to: '/docs/documents/document-upload',
  },
  {
    index: '04',
    kind: 'Conditional / decision',
    name: 'Customer registration',
    note: 'Already registered: continue with the customer code you hold. New customer: register now, or on the fly during Payout.',
    to: '/docs/customers/customer-registration',
  },
  {
    index: '05',
    kind: 'Preparation / reference',
    name: 'Bank and reference data',
    note: 'Bank List for the beneficiary bank, plus the master values your transaction type and route require.',
    to: '/docs/master-apis',
  },
  {
    index: '06',
    kind: 'Core transaction API',
    name: 'Payout',
    note: 'Submit the payout request.',
    to: '/docs/payout/payout',
  },
  {
    index: '07',
    kind: 'Core transaction API',
    name: 'Transaction Enquiry',
    note: 'Retrieve the state of the transaction.',
    to: '/docs/transactions/transaction-enquiry',
  },
  {
    index: '08',
    kind: 'Final / supporting',
    name: 'Balance',
    note: 'The final API in the documented sequence; retrieves the current balance.',
    to: '/docs/balance/balance-enquiry',
  },
];

const ENTRY_POINTS = [

  {
    kicker: 'Get started',
    title: 'Authentication and integration basics',
    body: 'Authenticate, obtain an access token, and learn the conventions this reference uses.',
    to: '/docs/authentication/authentication',
  },
  {
    kicker: 'API reference',
    title: 'Explore RHUB API contracts',
    body: 'Every documented API, with its method and endpoint, in a single index.',
    to: '/docs/api-index',
  },
  {
    kicker: 'Integration flow',
    title: 'Plan your integration',
    body: 'Where the customer, document and reference decisions apply across a payout.',
    to: '/docs/getting-started/integration-flow',
  },
  {
    kicker: 'Errors and validation',
    title: 'Result codes and field requirements',
    body: 'Current API error codes, transaction status codes and correspondent validation rules.',
    to: '/docs/errors',
  },
];

const CAPABILITIES = [
  {
    kicker: 'Customers',
    title: 'Customer Registration',
    body: 'Register business and individual customers, and obtain the customer code used at payout.',
    to: '/docs/customers/customer-registration',
  },
  {
    kicker: 'Documents',
    title: 'Document Upload',
    body: 'KYC/KYB verification documents and, for business transactions, invoice documentation.',
    to: '/docs/documents/document-upload',
  },
  {
    kicker: 'Wallets',
    title: 'WPT Payout',
    body: 'Wallet payout transactions, documented separately from bank payout.',
    to: '/docs/payout/wpt-payout',
  },
  {
    kicker: 'Balance',
    title: 'Balance Enquiry',
    body: 'Retrieve the current wallet or account balance.',
    to: '/docs/balance/balance-enquiry',
  },
  {
    kicker: 'Virtual Accounts',
    title: 'VA customer onboarding',
    body: 'Currencies, document requirements, individual and business registration, request status.',
    to: '/docs/virtual-accounts',
  },
  {
    kicker: 'Reference data',
    title: '14 master APIs',
    body: 'Remittance purpose, source of fund, relationship, occupation, bank list, wallet list and more.',
    to: '/docs/master-apis',
  },
  {
    kicker: 'Validation',
    title: 'Currency and country rules',
    body: 'Correspondent-specific conditional field requirements for LOCAL and SWIFT rails.',
    to: '/docs/validation/currency-validations',
  },
];

function Hero() {
  return (
    <header className="rhub-hero">
      <div className="container">
        {/* Official RHUB logo supplied by RHUB; rendered at a fixed height with
            width:auto so the 396x67 aspect ratio is preserved. */}
        <img
          className="rhub-hero__logo"
          src={useBaseUrl('img/rhub.png')}
          alt="RemittancesHub — Cross Border Business Payments"
          width={396}
          height={67}
        />
        <span className="rhub-eyebrow">RHUB Developer Portal 1.0</span>
        <h1>Integrate cross-border payouts with the RemittancesHub API</h1>
        <p>
          RemittancesHub (RHUB) is a licensed financial institution operating an Alternate Cross
          Border Network for inbound and outbound payments, enabling international fund transfers
          into bank accounts of beneficiaries. Integration uses REST APIs with JSON request and
          response payloads.
        </p>
        <div className="rhub-cta-row">
          <Link className="button button--primary button--lg" to="/docs/getting-started/integration-flow">
            Start with the integration flow
          </Link>
          <Link className="button button--secondary button--outline button--lg" to="/docs/api-index">
            Browse the API index
          </Link>
        </div>
        <Link className="rhub-hero__search" to="/search">
          <span className="rhub-hero__search-icon" aria-hidden="true">⌕</span>
          <span className="rhub-hero__search-text">
            Search the documentation — endpoints, fields, error codes
          </span>
        </Link>
      </div>
    </header>
  );
}

function Journey() {
  return (
    <section className="rhub-section">
      <div className="container">
        <span className="rhub-eyebrow">Payout journey</span>
        <h2>What it takes to complete a payout</h2>
        <p className="rhub-journey__lede">
          Not every stage is an API call. The core transaction APIs are labelled as such; the
          others are preparation, decisions or reference data that depend on the customer and
          the transaction type. A quotation does not need a registered customer — send an
          existing customer code, or send it blank and register later.
        </p>
        <ol className="rhub-stages">
          {JOURNEY.map((stage) => (
            <li key={stage.index} className="rhub-stage">
              <span className="rhub-stage__index">{stage.index}</span>
              <span className="rhub-stage__kind">{stage.kind}</span>
              <Link className="rhub-stage__name" to={stage.to}>
                {stage.name}
              </Link>
              <p className="rhub-stage__note">{stage.note}</p>
            </li>
          ))}
        </ol>
        <p className="rhub-journey__more">
          <Link to="/docs/getting-started/integration-flow">
            See the detailed integration flow
          </Link>{' '}
          for exactly where each decision and conditional requirement applies.
        </p>
      </div>
    </section>
  );
}

function EntryPoints() {
  return (
    <section className="rhub-section">
      <div className="container">
        <span className="rhub-eyebrow">Start here</span>
        <h2>Choose where to go</h2>
        <div className="rhub-grid">
          {ENTRY_POINTS.map((c) => (
            <Link key={c.title} className="rhub-card" to={c.to}>
              <span className="rhub-card__kicker">{c.kicker}</span>
              <h3>{c.title}</h3>
              <p>{c.body}</p>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

const REFERENCE_LINKS = [
  {label: 'API environments', to: '/docs/getting-started/environments'},
  {label: 'How to read this reference', to: '/docs/getting-started/conventions'},
  {label: 'Transaction flows', to: '/docs/getting-started/transaction-flows'},
  {label: 'Quotation', to: '/docs/quotation/quotation'},
  {label: 'Payout', to: '/docs/payout/payout'},
  {label: 'Transaction Enquiry', to: '/docs/transactions/transaction-enquiry'},
  {label: 'Payin Notification', to: '/docs/transactions/payin-notification'},
  {label: 'Current API error codes', to: '/docs/errors/current-error-codes'},
  {label: 'Transaction status codes', to: '/docs/errors/transaction-status-codes'},
  {label: 'Country validations', to: '/docs/validation/country-validations'},
];

function Reference() {
  return (
    <section className="rhub-section rhub-section--tight">
      <div className="container">
        <span className="rhub-eyebrow">Reference</span>
        <h2>Jump straight to a page</h2>
        <ul className="rhub-reflinks">
          {REFERENCE_LINKS.map((l) => (
            <li key={l.to}>
              <Link to={l.to}>{l.label}</Link>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}

function Capabilities() {
  return (
    <section className="rhub-section">
      <div className="container">
        <span className="rhub-eyebrow">Supporting capabilities</span>
        <h2>What else you can integrate</h2>
        <div className="rhub-grid">
          {CAPABILITIES.map((c) => (
            <Link key={c.title} className="rhub-card" to={c.to}>
              <span className="rhub-eyebrow">{c.kicker}</span>
              <h3>{c.title}</h3>
              <p>{c.body}</p>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home() {
  return (
    <Layout
      title="RHUB Developer Portal"
      description="Developer documentation for the RHUB (RemittancesHub) cross-border remittance APIs: authentication, quotation, payout, transaction enquiry, master data and validation rules.">
      <Hero />
      <EntryPoints />
      <Journey />
      <Capabilities />
      <Reference />
    </Layout>
  );
}
