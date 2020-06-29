%global srcname authres

Name:           python-%{srcname}
Version:        1.2.0
Release:        7%{?dist}
Summary:        Authentication Results Header Module
License:        ASL 2.0
URL:            https://launchpad.net/authentication-results-python
Source0:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz
Source1:	https://launchpad.net/authentication-results-python/1.2/%{version}/+download/%{srcname}-%{version}.tar.gz.asc
Source2:	https://db.debian.org/fetchkey.cgi?fingerprint=E7729BFFBE85400FEEEE23B178D7DEFB9AD59AF1#/GPG-KEY-kitterman
BuildArch:      noarch
BuildRequires:	gnupg2

%global _description\
RFC 8601 Authentication-Results Headers generation and parsing for\
Python/Python3.  See README for extension RFCs implemented.

%description %_description

%package -n python3-%{srcname}
Summary: %summary
BuildRequires: python3-devel python3-setuptools

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{python3} -m authres


%files -n python3-%{srcname}
%license COPYING
%doc CHANGES README
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/


%changelog
* Wed May 27 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.9

* Tue May 26 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-6
- Add upstream signature verification

* Sat May 16 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-5
- Rename spec to python-authres.spec

* Mon May 11 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-4
- Remove python2 support from spec for rawhide.  Can add to older branches.

* Fri May  8 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-3
- Add check section, fix reviewer notes, update current RFC, py2 conditional

* Wed May  6 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-2
- Support python2 as well

* Wed May  6 2020 Stuart Gathman <stuart@gathman.org> 1.2.0-1
- Latest upstream release

* Sun Apr 28 2013 Stuart Gathman <stuart@gathman.org> 0.601-1
- When stringifying RFC 5451 property values (pvalue), format them as quoted-
  strings if they contain spaces or special characters (and are not e-mail
  addresses). E.g., IPv6 addresses in policy.iprev properties must be
  double-quoted.
- Fix broken references to quoted_string variable in authres.core.
  AuthenticationResultsHeader._parse_pvalue method. (Closes: LP #1165978)
- Fix erroneous reference to ArgumentError exception to refer to ValueError
  instead. When does the Ruby compatiblity layer for Python come out?
- Added additional tests/examples in authres/tests

* Fri Apr 26 2013 Stuart Gathman <stuart@gathman.org> 0.600-2
- Include fixes for quoting problems

* Fri Apr 26 2013 Stuart Gathman <stuart@gathman.org> 0.600-1
- Update to 0.600, with patches for missing ArgumentError definition.

* Thu Feb 02 2010 Stuart Gathman <stuart@bmsi.com> 0.3-1
- Python-2.6 RPM

