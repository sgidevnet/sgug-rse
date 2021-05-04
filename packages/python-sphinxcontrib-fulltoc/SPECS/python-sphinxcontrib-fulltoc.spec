%global srcname sphinxcontrib-fulltoc
%global sum Include a full table of contents in your Sphinx HTML sidebar
%global desc sphinxcontrib-fulltoc is an extension for the Sphinx \
documentation system that changes the HTML output to include a more detailed \
table of contents in the sidebar. By default Sphinx only shows the local \
headers for the current page. With the extension installed, all of the page \
titles are included, and the local headers for the current page are also \
included in the appropriate place within the document.


Name: python-%{srcname}
Version: 1.2
Release: 9%{?dist}
Summary: %{sum}
License: ASL 2.0
URL: https://github.com/sphinxcontrib/%{srcname}
Source0: https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.0.tar.gz
Patch0: Don-t-invoke-Python-to-check-version.patch
BuildArch: noarch


%description
%{desc}


%package -n python3-%{srcname}
Summary: %{sum}
BuildRequires: python3-devel
BuildRequires: python3-pbr
Requires: python3-sphinx
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}


%package -n python-%{srcname}-doc
Summary: %{sum}
BuildRequires: python3-sphinx
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python-%{srcname}-doc
%{desc}

This package contains the documentation for sphinxcontrib-fulltoc.


%prep
%autosetup -p1 -n %{srcname}-%{version}.0
rm -rf *.egg-info


%build
%py3_build
make SPHINXBUILD=sphinx-build-3 -C docs html PYTHONPATH=$(pwd)
make SPHINXBUILD=sphinx-build-3 -C docs man PYTHONPATH=$(pwd)
rm docs/build/html/.buildinfo


%install
%py3_install

# Install the man pages
install -p -D -T -m 0644 docs/build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/python3-%{srcname}.1


%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS ChangeLog announce.rst
%{_mandir}/man1/python3-%{srcname}.1*
%{python3_sitelib}/*


%files -n python-%{srcname}-doc
%license LICENSE
%doc docs/build/html/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Jeremy Cline <jeremy@jcline.org> - 1.2-8
- Drop Python 2 sub-package

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2-6
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 13 2018 Jeremy Cline <jeremy@jcline.org> - 1.2-4
- Switch to the sdist tarball to build

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 Jeremy Cline <jeremy@jcline.org> - 1.2-1
- Update to the latest upstream.
- Turn the description to a macro.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1-4
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Jeremy Cline <jeremy@jcline.org> 1.1-2
- Added a -doc subpackage

* Sat Dec 12 2015 Jeremy Cline <jeremy@jcline.org> 1.1-1
- Initial release
