Name:           python-fisx
Version:        1.1.6
Release:        7%{?dist}
Summary:        Calculate x-ray fluorescence intensities

License:        MIT
URL:            https://github.com/vasole/fisx
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  %py3_dist cython
BuildRequires:  %py3_dist numpy

%global _description %{expand:
Calculate expected x-ray fluorescence intensities. The library accounts
for secondary and tertiary excitation, K, L and M shell emission lines
and de-excitation cascade effects.}

%description %_description

%package     -n python3-fisx
Summary: %summary

%description -n python3-fisx %_description

%prep
%autosetup -n fisx-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %__python3 -m fisx.tests.testAll

%files -n python3-fisx
%license LICENSE
%doc README.rst
%{python3_sitearch}/fisx/
%{python3_sitearch}/fisx-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.6-2
- Rebuild for F30.

* Tue Apr 30 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.6-1
- Initial packaging
