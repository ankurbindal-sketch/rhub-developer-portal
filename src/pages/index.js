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

const SEQUENCE = [
  {
    index: 'Step 01',
    name: 'Login (Authentication)',
    note: 'Required to authenticate and obtain access tokens for subsequent calls.',
    to: '/docs/authentication/authentication',
  },
  {
    index: 'Step 02',
    name: 'Quotation',
    note: 'Used to fetch the exchange rate and charges before initiating a payout.',
    to: '/docs/quotation/quotation',
  },
  {
    index: 'Step 03',
    name: 'Payout',
    note: 'Initiates the fund transfer based on the selected quotation and beneficiary.',
    to: '/docs/payout/payout',
  },
  {
    index: 'Step 04',
    name: 'Transaction Enquiry',
    note: 'Used to check the status of a previously initiated payout.',
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
    title: 'The source-backed API sequence',
    body: 'The call sequence RHUB supports, and which APIs are called based on the need.',
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
    body: 'Register business and individual customers, with the full source field contract for both.',
    to: '/docs/customers/customer-registration',
  },
  {
    kicker: 'Documents',
    title: 'Document Upload',
    body: 'Upload customer-related documents, including ID proofs and invoices.',
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

function Rail() {
  return (
    <section className="container rhub-rail">
      <div className="rhub-rail__label">
        <span className="rhub-eyebrow">The documented call sequence</span>
      </div>
      <div className="rhub-rail__track">
        {SEQUENCE.map((stop) => (
          <Link key={stop.name} className="rhub-stop" to={stop.to}>
            <span className="rhub-stop__index">{stop.index}</span>
            <span className="rhub-stop__name">{stop.name}</span>
            <p className="rhub-stop__note">{stop.note}</p>
          </Link>
        ))}
      </div>
      <p className="rhub-stop__note" style={{marginTop: '1.5rem'}}>
        The source states that the API call sequence is limited to the Login API, Quotation API,
        Payout API and Transaction Enquiry API, and that the remaining APIs — including bank list,
        document upload, balance and the master APIs — can be called based on the need.{' '}
        <Link to="/docs/getting-started/integration-flow">See the full sequence</Link>.
      </p>
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
            rule, status code, error code and example in this portal comes from the authoritative
            RHUB documentation source. Nothing has been inferred from general API conventions.
          </p>
          <p>
            Where the source does not establish something — a missing example, an unavailable
            diagram, an internal link with no target, or two source files that disagree — the page
            says <strong>REVIEW REQUIRED</strong> and the gap is catalogued in the{' '}
            <Link to="/docs/appendix/source-notes">source coverage notes</Link> rather than filled
            in. Rate limits, idempotency, retries, webhooks and SDKs are not documented by the
            source and so are absent here.
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
      <Rail />
      <Capabilities />
      <Fidelity />
    </Layout>
  );
}
