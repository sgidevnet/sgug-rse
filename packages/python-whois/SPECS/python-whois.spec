%global pypi_name whois

%global pypi_description Python wrapper for the "whois" command with \
a simple interface to access parsed WHOIS data for a given domain, \
able to extract data for all the popular TLDs (com, org, net, biz, info...).

Name: python-%{pypi_name}
Summary: Python module for retrieving WHOIS information of domains
License: MIT

Version: 0.9.7
Release: 2%{?dist}

URL: https://github.com/DannyCork/python-whois/
Source0: %pypi_source

BuildArch: noarch
BuildRequires: python3-devel

Requires: whois

%description
%pypi_description


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%pypi_description


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python3-%{pypi_name}
%license license
%doc README
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.7-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.7-1
- Update to version 0.9.7

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.6-2
- Include the README in the package

* Thu Feb 27 2020 Artur Iwicki <fedora@svgames.pl> - 0.9.6-1
- Initial packaging
