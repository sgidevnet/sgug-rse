%global pypi_name email-validator

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        A robust email syntax and deliverability validation library

License:        CC0
URL:            https://github.com/JoshData/python-email-validator
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This library validates that address are of the form x@y.com. This is the sort
of validation you would want for a login form on a website.

Key features:

- Good for validating email addresses used for logins/identity.
- Friendly error messages when validation fails (appropriate to show to end
  users).
- (optionally) Checks deliverability: Does the domain name resolve?
- Supports internationalized domain names and (optionally) internationalized
  local parts.
- Normalizes email addresses (important for internationalized addresses!).

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-dns
BuildRequires:  python3-idna
BuildRequires:  python3-coverage
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library validates that address are of the form x@y.com. This is the sort
of validation you would want for a login form on a website.

Key features:

- Good for validating email addresses used for logins/identity.
- Friendly error messages when validation fails (appropriate to show to end
  users).
- (optionally) Checks deliverability: Does the domain name resolve?
- Supports internationalized domain names and (optionally) internationalized
  local parts.
- Normalizes email addresses (important for internationalized addresses!).

%prep
%autosetup -n python-%{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests \
  -k "not test_deliverability"

%files -n python3-%{pypi_name}
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/email_validator
%{python3_sitelib}/email_validator/
%{python3_sitelib}/email_validator-%{version}-py*.egg-info

%changelog
* Wed Jun 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Enable tests
- Update to new upstream release 1.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.5-2
- Implement changes from rhbz#1787419 to match rhbz#1733683

* Mon Jan 06 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5.
- Review fixes.

* Sat Jul 27 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.0.4-1
- Initial package.
