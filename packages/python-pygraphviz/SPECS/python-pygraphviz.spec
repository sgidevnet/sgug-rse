Name:           python-pygraphviz
Version:        1.5
Release:        5%{?dist}
Summary:        Create and Manipulate Graphs and Networks
License:        BSD
URL:            http://networkx.lanl.gov/pygraphviz/
Source0:        https://github.com/pygraphviz/pygraphviz/archive/pygraphviz-%{version}.tar.gz
# Fix a few types in the swig interface
# https://github.com/pygraphviz/pygraphviz
Patch0:         pygraphviz-swig.patch

# https://github.com/pygraphviz/pygraphviz/pull/191
Patch0001:      0001-doc-use-add_object_type-instead-of-deprecated-add_de.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  graphviz-devel
BuildRequires:  swig

%global _description                                                  \
PyGraphviz is a Python interface to the Graphviz graph layout and     \
visualization package. With PyGraphviz you can create, edit, read,    \
write, and draw graphs using Python to access the Graphviz graph data \
structure and layout algorithms. PyGraphviz is independent from       \
NetworkX but provides a similar programming interface.

%description %_description

%package -n python3-pygraphviz
Summary:        %{summary}
%{?python_provide:%python_provide python3-pygraphviz}

%description -n python3-pygraphviz %_description

This package contains the version for Python 3.

%package doc
Summary:        Documentation for pygraphviz
Provides:       bundled(jquery)
BuildArch:      noarch

%description doc
Documentation for PyGraphViz.

%prep
%autosetup -p1 -n pygraphviz-pygraphviz-%{version}

# Regenerate the swig-generated files
swig -python pygraphviz/graphviz.i

# Fix the shebangs in the examples
for fil in examples/*.py; do
  sed -i.orig 's,%{_bindir}/env python,%{__python3},' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
%py3_build

# docs
%make_build -C doc html PYTHONPATH=$(pwd)/build/lib.%{python3_platform}-%{python3_version}

%install
%py3_install
mv %{buildroot}%{_docdir}/pygraphviz-* %{buildroot}%{_pkgdocdir}
rm %{buildroot}%{_pkgdocdir}/INSTALL.txt
cp -p README.rst %{buildroot}%{_pkgdocdir}
rm doc/build/html/.buildinfo
cp -av doc/build/html %{buildroot}%{_pkgdocdir}/
chmod g-w %{buildroot}%{python3_sitearch}/pygraphviz/_graphviz.*.so

%global _docdir_fmt %{name}

%files -n python3-pygraphviz
%{python3_sitearch}/pygraphviz*
%exclude %{python3_sitearch}/pygraphviz/graphviz_wrap.c
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README.rst
%license LICENSE

%files doc
%doc %dir %{_pkgdocdir}
%doc %{_pkgdocdir}/html
%doc %{_pkgdocdir}/examples
%license LICENSE

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr  4 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5-4
- Fix build under sphinx 2.x (#1696133)

* Sun Feb 17 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5-3
- Restore the tests subpackage (#1677978)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Jerry James <loganjerry@gmail.com> - 1.5-1
- Update to latest version
- Drop nose requirement; only needed to run tests, not to use the package
- Add swig patch to fix type-related compiler warnings
- Regenerate the swig files
- Do not ship the test code or the swig-generated C file
- Build sphinx docs with python3 instead of python2
- Ship LICENSE file with all packages
- Fix shebang in example code

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-3.rc2.11
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.rc2.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3-3.rc2.9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3-3.rc2.8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.rc2.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3-3.rc2.6
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.rc2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.rc2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.rc2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3-3.rc2.2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3.rc2.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr  5 2016 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-3.rc2
- Rename python2 subpackage to python2-pygraphviz
- Fix Requires (#1324237)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2.rc2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2.rc2.2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 30 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3-2rc2
- Reformat version string to follow guidelines for pre-release versions

* Sat Nov 29 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-2
- Fixed after review: use more macros, include directories in %%files,
  add provides for bundled jquery, remove empty file.

* Mon Nov 24 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3rc2-1
- Update to latest version, build sphinx docs, add python3 subpackage.

* Wed Oct 26 2011 Vedran Miletić <rivanvx@gmail.com> - 1.1-1
- Initial package.
