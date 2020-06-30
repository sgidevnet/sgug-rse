%global srcname ifaddr
%global _description \
ifaddr is a small Python library that allows you to find all the IP addresses\
of the computer.

Name:           python-%{srcname}
Version:        0.1.6
Release:        7%{?dist}
Summary:        Python library that allows you to find all the IP addresses of the computer

# https://github.com/pydron/ifaddr/pull/18
License:        MIT
URL:            https://pypi.org/project/ifaddr/
Source:         %{pypi_source}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.6-1
- Initial package
