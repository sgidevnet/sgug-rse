%global pypi_name launchpadlib
Name:           python-%{pypi_name}
Version:        1.10.13
Release:        2%{?dist}
Summary:        Script Launchpad through its web services interfaces

License:        LGPLv3
URL:            https://launchpad.net/launchpadlib 
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
Launchpadlib is an open-source Python library that lets you treat the HTTP
resources published by Launchpad's web service as Python objects responding
to a standard set of commands. With launchpadlib you can integrate your
applications into Launchpad without knowing a lot about HTTP client
programming.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(httplib2)
BuildRequires:  python3dist(keyring)
BuildRequires:  python3dist(lazr.restfulclient) >= 0.9.19
BuildRequires:  python3dist(lazr.uri)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(testresources)
BuildRequires:  python3dist(wadllib)

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license COPYING.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.10.13-2
- Rebuilt for Python 3.9

* Mon Apr 20 2020 Ondřej Pohořelský <opohorel@redhat.com> - 1.10.13-1
- Update to 1.10.13

* Fri Apr 17 2020 Ondřej Pohořelský <opohorel@redhat.com> - 1.10.12-1
- Update to 1.10.12

* Thu Apr 16 2020 Ondřej Pohořelský <opohorel@redhat.com> - 1.10.11-1
- Update to 1.10.11
- Fix URL in spec file

* Tue Feb 4 2020 Ondřej Pohořelský <opohorel@redhat.com> - 1.10.10-1
- Update to 1.10.10

* Mon Feb 3 2020 Ondřej Pohořelský <opohorel@redhat.com> - 1.10.9-1
- Update to 1.10.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.10.7-1
- Initial package
