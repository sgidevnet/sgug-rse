# Lots of tests fail, even in a clean pip environment
%bcond_with tests

%global _description %{expand: \
PyBIDS is a Python module to interface with datasets conforming BIDS.
}

%global srcname     pybids

Name:       python-%{srcname}
Version:    0.10.2
Release:    2%{?dist}
Summary:    Interface with datasets conforming to BIDS

License:    MIT
URL:        http://bids.neuroimaging.io
Source0:    https://github.com/INCF/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description
%{_description}

%package -n python3-%{srcname}
Summary:    Interface with datasets conforming to BIDS
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist grabbit} >= 0.2.5
BuildRequires:  %{py3_dist num2words}
BuildRequires:  %{py3_dist duecredit}
BuildRequires:  %{py3_dist nibabel}
BuildRequires:  %{py3_dist patsy}
BuildRequires:  %{py3_dist bids-validator}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist sqlalchemy}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{_description}

%package doc
Summary:    Interface with datasets conforming to BIDS
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist m2r}
BuildRequires:  %{py3_dist numpydoc}

%description doc
Description for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

# stray backup file?
rm -rf *.egg-info

# Remove bundled six and inflect
rm -rf bids/external

pushd bids
    sed -ibackup 's/from.*external import/import/' layout/{layout,index,models}.py utils.py
popd


%build
%py3_build

pushd doc && \
    sphinx-build-3 . html
    rm -fv .buildinfo
popd


%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=. py.test-3 -s -v -k-test_split .
%endif

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info
%{python3_sitelib}/bids/

%files doc
%doc examples/ doc/html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.10.2-1
- Update to 0.10.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 12 2019 Aniket Pradhan <major@fedoraproject.org> - 0.10.0-1
- Bumped to v0.10.0

* Tue Oct 1 2019 Aniket Pradhan <major@fedoraproject.org> - 0.9.4-1
- Bumped to v0.9.4

* Thu Aug 22 2019 Aniket Pradhan <aniket17133@iiitd.ac.in> - 0.9.3-1
- Bumped to v0.9.3

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.9.1-1
- Update to 0.9.1

* Mon Apr 08 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.0-1
- Update the latest release
- Drop dropped grabbit dep
- Add new BR: python-bids-validator: requires review: 1697498
- Unbundle new bundled libs

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-3.gite35ced6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.5-2.gite35ced6
- Use bconds

* Wed Nov 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.5-1.gite35ced6
- Use latest git snapshot that fixes tests
- Add documentation and examples in subpackage

* Wed Nov 07 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.3-2
- Enable tests now that duecredit is available in rawhide
- Disable py2 build since python-nibabel is only py3 even in F29

* Fri Jul 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.3-1
- Update to latest release
- Use py.test
- Disable tests until nibabel is fixed

* Mon Jan 15 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-2
- Use github source for license and test suite
- Fix requires and build requires

* Fri Jan 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.4.2-1
- Initial build
