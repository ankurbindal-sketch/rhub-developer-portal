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
    note: 'Obtain the access token every other call depends on.',
    to: '/docs/authentication/authentication',
  },
  {
    index: '02',
    kind: 'Preparation / decision',
    name: 'Customer',
    note: 'Existing customer: use the customer code you hold. New customer: register beforehand, or on the fly during Payout.',
    to: '/docs/customers/customer-registration',
  },
  {
    index: '03',
    kind: 'Preparation',
    name: 'KYC / KYB',
    note: 'Required for payout — KYC for individual customers, KYB for business customers. Payout carries the reference in docReferenceNumber.',
    to: '/docs/documents/document-upload',
  },
  {
    index: '04',
    kind: 'Core transaction API',
    name: 'Quotation',
    note: 'Obtain the rate, charges and quote identifier for the transaction.',
    to: '/docs/quotation/quotation',
  },
  {
    index: '05',
    kind: 'Conditional / decision',
    name: 'Transaction documents',
    note: 'C2C: no invoice-document requirement. B2B, B2C and C2B: invoice required, referenced by sendClientTrxReference.',
    to: '/docs/documents/document-upload',
  },
  {
    index: '06',
    kind: 'Conditional / reference',
    name: 'Reference data',
    note: 'As required by route or correspondent — Bank List, other master APIs, currency and country validations.',
    to: '/docs/master-apis',
  },
  {
    index: '07',
    kind: 'Core transaction API',
    name: 'Payout',
    note: 'Submit the payout request.',
    to: '/docs/payout/payout',
  },
  {
    index: '08',
    kind: 'Core transaction API',
    name: 'Transaction Enquiry',
    note: 'Check the status of the payout.',
    to: '/docs/transactions/transaction-enquiry',
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
          Not every stage is an API call. Four stages are the core transaction APIs; the
          others are preparation, decisions or reference data that depend on the customer and
          the transaction type. Each stage is labelled accordingly.
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

function Fidelity() {
  return (
    <section className="rhub-section">
      <div className="container">
        <span className="rhub-eyebrow">Documentation fidelity</span>
        <h2>What this portal does and does not claim</h2>
        <div className="rhub-note">
          <p>
            Every endpoint, HTTP method, field name, type, length, requirement flag, validation
            rule, status code, error code and example comes from RHUB: the documentation source,
            current supplemental data such as the error-code reference, and operational guidance
            confirmed by the RHUB team. Nothing has been inferred from general API conventions.
          </p>
          <p>
            Where RHUB has not established something, the page says{' '}
            <strong>REVIEW REQUIRED</strong> rather than filling the gap. Rate limits,
            idempotency, retries, webhooks and SDKs are not part of the RHUB API documentation, so
            they are absent here. See{' '}
            <Link to="/docs/getting-started/conventions">how to read this reference</Link>.
          </p>
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
      <Fidelity />
    </Layout>
  );
}
