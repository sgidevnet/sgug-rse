%bcond_without check

%global srcname signedjson

Name:           python-%{srcname}
Version:        1.1.1
Release:        2%{?dist}
Summary:        Sign JSON with Ed25519 signatures

License:        ASL 2.0
URL:            https://github.com/matrix-org/python-signedjson
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Features:
* More than one entity can sign the same object.
* Each entity can sign the object with more than one key making it easier
  to rotate keys
* ED25519 can be replaced with a different algorithm.
* Unprotected data can be added to the object under the "unsigned" key.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%if %{with check}
BuildRequires:  python3-nose
BuildRequires:  python3dist(canonicaljson) >= 1
BuildRequires:  python3dist(unpaddedbase64) >= 1.0.1
BuildRequires:  python3dist(pynacl) >= 0.3
BuildRequires:  python3dist(typing-extensions) >= 3.5
%endif

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vr *.egg-info
# This is standard thing in 3.8+
sed -i -e "/importlib_metadata/d" setup.py
sed -i -e "s/importlib_metadata/importlib.metadata/" %{srcname}/__init__.py

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
nosetests-%{python3_version} -v
%endif

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.9

* Thu Apr 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Wed Feb 19 2020 Dan Callaghan <djc@djc.id.au> - 1.1.0-1
- Upstream release 1.1.0 (RHBZ#1796270)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-9
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-3
- Fix typo in Requires

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.0-1
- Initial package
