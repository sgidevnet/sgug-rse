%global         srcname  zeep
%global         desc     Zeep inspects the WSDL document and generates the corresponding\
code to use the services and types in the document. This\
provides an easy to use programmatic interface to a SOAP server.

Name:           python-%{srcname}
Version:        3.4.0
Release:        5%{?dist}
Summary:        A fast and modern Python SOAP client

License:        MIT and BSD
URL:            https://github.com/mvantellingen/python-zeep
Source0:        %pypi_source

BuildArch:      noarch

# required for py3_build macro
BuildRequires:  python3-devel

BuildRequires:  python3-setuptools


# from setup.py
BuildRequires: python3-appdirs >= 1.4.0
BuildRequires: python3-attrs >= 17.2.0
BuildRequires: python3-cached_property >= 1.3.0
BuildRequires: python3-defusedxml >= 0.4.1
BuildRequires: python3-isodate >= 0.5.4
BuildRequires: python3-lxml >= 3.1.0
BuildRequires: python3-requests >= 2.7.0
BuildRequires: python3-requests-toolbelt >= 0.7.1
BuildRequires: python3-six >= 1.9.0
BuildRequires: python3-pytz

## for tests
BuildRequires: python3-freezegun >= 0.3.8
BuildRequires: python3-mock >= 2.0.0
BuildRequires: python3-pretend >= 1.0.8
BuildRequires: python3-pytest-cov >= 2.5.1
BuildRequires: python3-pytest >= 3.1.3
BuildRequires: python3-requests-mock >= 0.7.0
BuildRequires: python3-pytest-tornado >= 0.4.5
BuildRequires: python3-aioresponses

%{?python_enable_dependency_generator}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -p1 -n %{srcname}-%{version}

# disable linting dependencies and exact test dependencies
sed -i -e "s/\('\(isort\|flake\)\)/# \1/"  -e "s/\('[A-Za-z_-]\+\)==/\1>=/"  setup.py

%build
%py3_build


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst examples
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*-py*.egg-info/


%changelog
* Fri Jun 26 2020 Georg Sauthoff <mail@gms.tf> - 3.4.0-5
- Be more explicit regarding setuptools depenency,
  cf. https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 3.4.0-2
- fix date format

* Sun Dec 08 2019 Georg Sauthoff <mail@gms.tf> - 3.4.0-1
- bump to latest upstream

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Georg Sauthoff <mail@gms.tf> - 3.3.1-1
- initial packaging
