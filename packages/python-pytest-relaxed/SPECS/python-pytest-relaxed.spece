%global srcname pytest-relaxed
%global desc  pytest-relaxed provides 'relaxed' test discovery for pytest. \
It is the spiritual successor to https://pypi.python.org/pypi/spec, but \
is built for pytest instead of nosetests, and rethinks some aspects of \
the design (such as a decreased emphasis on the display side of things.)

Name: python-%{srcname}
Version: 1.1.5
Release: 9%{?dist}
Summary: Relaxed test discovery for pytest

License: BSD
URL: https://github.com/bitprophet/pytest-relaxed
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel 
BuildRequires: %{py3_dist decorator}
BuildRequires: %{py3_dist pytest} < 5
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist six}
# No need to specify runtime dependencies because they'll be auto-generated

%description -n python3-%{srcname}
%{desc}

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version}

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/pytest_relaxed-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/pytest_relaxed/

%changelog
* Sat May 30 2020 Paul Howarth <paul@city-fan.org> - 1.1.5-9
- Avoid FTBFS with pytest 5

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-6
- Make the release strictly bigger than the last two builds (rhbz #1788771)

* Mon Oct 07 2019 Othman Madjoudj <athmane@fedoraproject.org> - 1.1.5-1
- Update to 1.1.5 (rhbz #1697355)

* Sun Oct 06 2019 Othman Madjoudj <athmane@fedoraproject.org> - 1.1.5-5
- Drop python2 subpackage (python2 eol)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Paul Howarth <paul@city-fan.org> - 1.1.5-1
- Update to 1.1.5
- Re-enable the test suite

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-6
- Rebuilt for Python 3.7

* Thu Jun 28 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.0.0-5
- Disable the test suite until a version compatible with pytest > 3.3 is available

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.0.0-2
- Minor packaging fixes

* Thu Nov 16 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 1.0.0-1
- Initial spec

