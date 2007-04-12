%define name 	libmatchbox
%define version 1.9

%define major 	1
%define libname %mklibname mb %major

Summary: 	Libraries for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	%mkrel 1
Url: 		http://projects.o-hand.com/matchbox/
License: 	GPL
Group: 		System/Libraries
Source: 	http://projects.o-hand.com/matchbox/sources/libmatchbox/%version/%{name}-%{version}.tar.bz2

BuildRequires:	XFree86-devel pango-devel png-devel jpeg-devel libXsettings-client-devel
Buildroot: 	%_tmppath/%name-%version-buildroot

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

%package -n	%libname
Group:		System/Libraries
Summary:	Inter-toolkit configuration settings

%description -n %libname
Libraries for the Matchbox Desktop.

%package -n %libname-devel
Group:          Development/C
Summary:        Static libraries and header files from %name
Provides:	matchbox-devel = %version-%release
Provides:       %name-devel = %version-%release
Provides:	lib%name-devel = %version-%release
Provides:	libmb-devel = %version-%release
Requires:       %libname = %version

%description -n %libname-devel
Static libraries and header files from %name

%prep
%setup -q

%build
%configure2_5x --enable-xsettings --enable-png --enable-jpeg --enable-pango
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_libdir/pkgconfig/*.pc
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_includedir/libmb/*.h


