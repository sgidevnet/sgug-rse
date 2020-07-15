# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

# Temporary values we need until higher level macros are in place
# (and they should be the same anyway)
%global rpmmacrodir %{_prefix}/lib/rpm/macros.d

Name:           python-rpm-macros
Version:        3
Release:        53%{?dist}
Summary:        The unversioned Python RPM macros

# macros: MIT, compileall2.py: PSFv2
License:        MIT and Python
Source0:        macros.python
Source1:        macros.python-srpm
Source2:        macros.python2
Source3:        macros.python3
Source4:        macros.pybytecompile
Source5:        https://github.com/fedora-python/compileall2/raw/v0.5.0/compileall2.py

BuildArch:      noarch
# For %%python3_pkgversion used in %%python_provide and compileall2.py
Requires:       python-srpm-macros >= 3-46
Obsoletes:      python-macros < 3
Provides:       python-macros = %{version}-%{release}

%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python-srpm-macros
Summary:        RPM macros for building Python source packages
Requires:       redhat-rpm-config

%description -n python-srpm-macros
RPM macros for building Python source packages.

%package -n python2-rpm-macros
Summary:        RPM macros for building Python 2 packages
Requires:       python-srpm-macros >= 3-38
# Would need to be different for each release - worth it?
#Conflicts:      python2-devel < 2.7.11-3

%description -n python2-rpm-macros
RPM macros for building Python 2 packages.

%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
Requires:       python-srpm-macros >= 3-38

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.


%prep

%build

%install
mkdir -p %{buildroot}%{rpmmacrodir}
install -m 644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
  %{buildroot}%{rpmmacrodir}/

mkdir -p %{buildroot}%{_rpmconfigdir}/sgug
install -m 644 %{SOURCE5} \
  %{buildroot}%{_rpmconfigdir}/sgug/

%files
%{rpmmacrodir}/macros.python
%{rpmmacrodir}/macros.pybytecompile

%files -n python-srpm-macros
%{rpmmacrodir}/macros.python-srpm
%{_rpmconfigdir}/sgug/compileall2.py

%files -n python2-rpm-macros
%{rpmmacrodir}/macros.python2

%files -n python3-rpm-macros
%{rpmmacrodir}/macros.python3


%changelog
* Sat Jun 06 2020 Daniel Hams <daniel.hams@gmail.com> - 3-53
- Move vendor to "sgug" so these macros are correctly picked up.

* Thu May 21 2020 Daniel Hams <daniel.hams@gmail.com> - 3-52
- Fix bashism in the pybyte compile macros file

* Sun Apr 12 2020 Daniel Hams <daniel.hams@gmail.com> - 3-51
- And Unxy + HAL too, getting some macros in place

* Sat Dec 28 2019 Miro Hrončok <mhroncok@redhat.com> - 3-51
- Define %%python, but make it work only if %%__python is redefined
- Add the %%pycached macro

* Tue Nov 26 2019 Lumír Balhar <lbalhar@redhat.com> - 3-50
- Update of bundled compileall2 module

* Fri Sep 27 2019 Miro Hrončok <mhroncok@redhat.com> - 3-49
- Define %%python2 and %%python3

* Mon Aug 26 2019 Miro Hrončok <mhroncok@redhat.com> - 3-48
- Drop --strip-file-prefix option from %%pyX_install_wheel macros, it is not needed

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Miro Hrončok <mhroncok@redhat.com> - 3-46
- %%python_provide: Switch python2 and python3 behavior
- https://fedoraproject.org/wiki/Changes/Python_means_Python3
- Use compileall2 module for byte-compilation with Python >= 3.4
- Do not allow passing arguments to Python during byte-compilation
- Use `-s` argument for Python during byte-compilation
