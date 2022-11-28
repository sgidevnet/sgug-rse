Name:           libbraiding
Version:        1.0
Release:        3%{?dist}
Summary:        Library for computations on braid groups

License:        GPLv2+
URL:            https://github.com/miguelmarco/libbraiding
Source0:        https://github.com/miguelmarco/libbraiding/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
This library allows various computations on braid groups, such as normal
forms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p0

# Fix the FSF's address
for fil in lib/*.{cpp,h}; do
  sed -i.orig 's/59 Temple Place, Suite 330, Boston, MA 02111-1307/51 Franklin Street, Suite 500, Boston, MA 02110-1335/' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

# Upstream does not generate the configure script
autoreconf -fi .

%build
%configure --disable-static

# Work around libtool reordering -Wl,--as-needed after all the libraries.
sed -i 's|CC=.g..|& -Wl,--as-needed|' libtool

%make_build

%install
%make_install

# We do not want the libtool files
rm -f %{buildroot}%{_libdir}/*.la

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.0.*

%files devel
%doc CHANGELOG
%{_includedir}/braiding.h
%{_includedir}/cbraid*.h
%{_libdir}/%{name}.so

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Jerry James <loganjerry@gmail.com> - 1.0-1
- Initial RPM
