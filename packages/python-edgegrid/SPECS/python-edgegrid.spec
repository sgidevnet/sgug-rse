%global srcname edgegrid-python

Summary: {OPEN} client authentication protocol for python-requests
Name: python-edgegrid
Version: 1.1.1
Release: 8%{?dist}
Source0: %{pypi_source}
License: ASL 2.0
BuildArch: noarch
URL: https://github.com/akamai-open/AkamaiOPEN-edgegrid-python

%{?python_enable_dependency_generator}

%description
This library implements an Authentication handler for requests
that provides the Akamai {OPEN} Edgegrid Authentication scheme.

%package -n python3-edgegrid
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%{?python_provide:%python_provide python3-edgegrid}

%description -n python3-edgegrid
This library implements an Authentication handler for requests
that provides the Akamai {OPEN} Edgegrid Authentication scheme.

%prep
%autosetup -n %{srcname}-%{version}

# Sources currently have some useless shebangs, and rpmlint
# doesn't like that.
# https://github.com/akamai/AkamaiOPEN-edgegrid-python/pull/35
# Let's patch them out for now.
find akamai -name '*.py' -exec sed -r -e 's|^#!/usr/bin/env.*|#|' -i '{}' ';'


%build
%py3_build

%install
%py3_install

%files -n python3-edgegrid
%doc README.rst
%license LICENSE

# Upstream installs a test suite, but it doesn't actually work.
# Probably was never intended to include this in the install.
# https://github.com/akamai/AkamaiOPEN-edgegrid-python/issues/36
%exclude %{python3_sitelib}/akamai/edgegrid/test/

%{python3_sitelib}/edgegrid_python*.egg-info/
%{python3_sitelib}/edgegrid_python*.pth
%dir %{python3_sitelib}/akamai
%{python3_sitelib}/akamai/edgegrid


%changelog
* Fri Jun 26 2020 Rohan McGovern <rmcgover@redhat.com> - 1.1.1-8
- Explicitly BuildRequires python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Rohan McGovern <rmcgover@redhat.com> - 1.1.1-2
- Ensure all directories owned
- Remove Group tag per guidelines
- Add python_provide per guidelines

* Wed Dec 19 2018 Rohan McGovern <rmcgover@redhat.com> - 1.1.1-1
- Initial RPM release
