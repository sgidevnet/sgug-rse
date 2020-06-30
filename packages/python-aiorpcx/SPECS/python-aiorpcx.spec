%global pypi_name aiorpcX
%global srcname aiorpcx
%global _description \
Transport, protocol and framing-independent async RPC client\
and server implementation.

Name:           python-%{srcname}
Version:        0.11.0
Release:        6%{?dist}
Summary:        Generic async RPC implementation

# https://github.com/kyuupichan/aiorpcX/issues/11
# aiorpcx/curio.py is BSD, rest is MIT
License:        MIT and BSD
URL:            https://pypi.org/project/aiorpcX/
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Thu Apr 04 2019 Jonny Heggheim <hegjon@gmail.com> - 0.10.5-2
- Changed python- prefix to python3-

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.5-1
- Initial package
