%global pypi_name lazr.restfulclient
Name:           python-lazr-restfulclient
Version:        0.14.3
Release:        2%{?dist}
Summary:        Programmable client library for lazr.restful web services

License:        LGPLv3
URL:            https://launchpad.net/lazr.restfulclient
Source0:        %{pypi_source}
BuildArch:      noarch

%global _description %{expand:
A programmable client library that takes advantage of the commonalities among
lazr.restful web services to provide added functionality on top of wadllib.}

%description %_description


%package -n     python3-lazr-restfulclient
Summary:        %{summary}
%{?python_provide:%python_provide python3-lazr-restfulclient}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# check is disabled, but we BR runtime dpes to make sure they exists:
BuildRequires:  python3dist(distro)
BuildRequires:  python3dist(httplib2) >= 0.7.7
BuildRequires:  python3dist(oauthlib)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(wadllib) >= 1.1.4

%description -n python3-lazr-restfulclient %_description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

#check
#lazr.restful test dependency not packaged
#{__python3} setup.py test

%files -n python3-lazr-restfulclient
%license COPYING.txt
%doc README.rst
%{python3_sitelib}/lazr
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.14.3-2
- Rebuilt for Python 3.9

* Wed Feb 5 2020 Ondřej Pohořelský <opohorel@redhat.com> - 0.14.3-1
- Update to 0.14.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.14.2-1
- Initial package
