%global pypi_name wadllib
Name:           python-%{pypi_name}
Version:        1.3.4
Release:        2%{?dist}
Summary:        Navigate HTTP resources using WADL files as guides

License:        LGPLv3
URL:            https://launchpad.net/wadllib
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A Python library to navigate HTTP resources using WADL files as guides.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(lazr.uri)

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
# README is installed in sitelib and used at runtime
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.4-2
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Ondřej Pohořelský <opohorel@redhat.com> - 1.3.4-1
- Update to 1.3.4 

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-1
- Initial package
